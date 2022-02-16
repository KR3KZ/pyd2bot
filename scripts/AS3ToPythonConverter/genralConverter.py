from audioop import lin2adpcm
import itertools
import os
import pathlib
import re
from time import perf_counter
from tqdm import tqdm

patterns = {
    "^\n?(\s*)public static function get(\S+)ById\(id:(?:uint|int|double)\)\s*:\s*(\S+)\n?\s*{\n?\s*return\s*GameData\.getObject\(\s*MODULE\s*,\s*id\s*\)\s*as\s*(\S+);\n?\s*}\n?$$": r"\n\1@classmethod\1def get\2ById(cls, id:int) -> '\3':\1\treturn GameData.getObject(cls.MODULE, id)\n",
    "^\n?(\s*)public static function get(\S+)s\(\)\s*:\s*Array\n?\s*{\n?\s*return\s*GameData\.getObjects\(\s*MODULE\s*\)\s*;\n?\s*}\n?$$": r"\n\1@classmethod\1def get\2s(cls) -> list['\2']:\1\treturn GameData.getObjects(cls.MODULE)\n",
    
    "for each\((\S+) in (.*)\)": r"for \1 in \2:",
    "\((\S+) as (\S+)\)": r"\1",
    
    "^\s*from com.ankamagames.jerakine.logger.Log import Log": "",
    "^\s*import com.ankamagames.jerakine.logger.Logger;": "from com.ankamagames.jerakine.logger.Logger import Logger",
    "package \S+\n?": "",
    
    "String\((.*?)\)": r"str(\1)",
    "^\s*import (\S+(?:\.\S+)*)\.(\S+);": r"from \1.\2 import \2",
    "getQualifiedobjectName\((\S+)\)": r"\1.__class__.__name__",
    "public ": "",
    "static ": "",
    "private ": "",
    "protected ": "",
    "const ": "",
    "final ": "",
    "override ": "",
    "new ": "",
    "var ": "",
    ";": "",
    "^(.*){(.*)\n?": "",
    "^(.*)}(.*)\n?": "",
    ":\*": "",
    " = null": " = None",
    "\:Number": ":float",
    "([\s|[|<])String([\s|]|>])": r"\1str\2",
    "void": "None",
    "Array": "list",
    "Boolean": "bool",
    "uint": "int",
    "false": "False",
    "true": "True",
    "\|\|": "or",
    "&&": "and",
    "this": "self",
    "NaN": "None",
    "tostr": "__str__",
    "Dictionary": "dict",
    "undefined": "None",
    "\.push": ".append",
    " implements ": " ",
    " extends ": " ",    

    
    "Vector\.<(\S+)>": r"list[\1]",
    "function (\S+)\((.*)\) : (\S+)": r"def \1(self, \2) -> \3:",
    "function (\S+)\((.*)\) :": r"def \1(self, \2):",
    # "if !(.*)": r"if not \1",
    "([_a-zA-Z][_a-zA-Z0-9.]{0,30})\.length": r"len(\1)",
    "throw Error(.*)": r"raise Exception\1",
    r'^(.*)function get (\S+)\((.*)\) : (\S+)$': r"\1@property\n\1def \2(self, \3) -> \4:",
    r'^(.*)function set (\S+)\((.*)\) : (\S+)$': r"\1@\2.setter\n\1def \2(self, \3) -> \4:",
    "function [A-Z]+(\S+)\((.*)\)": r"def __init__(self, \2):",
    "_log:Logger = Log\.getLogger\((.*)\)": r'logger = Logger(__name__)',
    ", \)": r")",
    "!==": r"is not",
    "!(\w+)": r"not \1",
    "delete ": r"del ",
    "_log.(info|error|debug)\((.*)\)": r"logger.\1(\2)",
    "else if": r"elif",
    "===": r"==",
    " (\S+).__str__\(\)$": r" str(\1)",
    "(\S+)\+\+": r"\1 += 1",
    "\.getInstance()": "",
    "Math.abs": "abs",
    "Math.max": "max",
    "Math.floor": "math.floor",
    "NameUtil.getUnqualifiedClassName(self)": "self.__class__.__name__",
    "Math.sqrt": "math.sqrt",
    "Math.PI": "math.pi",
    "Math.min": "min",
    r"(if|else\sif|else)\s*\((.*)\)\s*\n": r"\1 \2:\n",
    r"(elif|if) (\S+) is ([A-Z]+\S+)\:": r"\1 isinstance(\2, \3):",

    r"super\((.*)\)": r"super().__init__(\1)",
    r"super\.": r"super().",
    r"(\S+).__str__\(\)": r"str(\1)",
    r"for (\S+):(\S+)\s*=\s*(\S+)\s+(\S+)\s+(.*)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\:": r"for \1 in range(\3, \6, \9):",
    r"Function" : "FunctionType",
    r"StringUtils\.replace\((.*),(.*),(.*)\)": r"str.replace(\1, \2, \3)",
    r"\.indexOf": ".find",
    r"\.substring\((.*?),(.*?)\)": r"[\1:\2]",
    r"\.substring\((.*)\)": r"[:\1]",
    r"catch\(e\:Error\)": "except Exception as e:",
    r"catch\(e\:(\S+)\)": r"except \1 as e:",
    r"try": "try:",
    r"_log": "logger",
    r"throw ([A-Z]+\S+)": r"raise \1",
    r"IDataInput": "ByteArray",
    r"/s*\:/s*Object": ":object",
    r"-> \*": "-> Any",
    r"([_a-zA-Z][_a-zA-Z0-9]{0,30})/s?:/s?Class": r"\1:object",
    r".concat": ".extend",
    r"([_a-zA-Z][_a-zA-Z0-9]{0,30}):String": r"\1:str",
    r"getTimer\(\)": "perf_counter()",
    r"\.shift\(\)": ".pop(0)",
    r"msg as (\w+)": r"msg",

    # extras only for items criterion
    "_operator": "self._operator",
    "_criterionValue": "self._criterionValue",
    "else$$": r"else:",
    # " as [A-Z]+\S+": "",
    # "(\S+) is ([A-Z]+\S+)": r"isinstance(\1, \2)",
    # "(\S+) ? (\S+) : (^[:\s]+)": r"\2 if \1 else \3",

}
SWITCH_CASE_PATTERN = r"\s*(switch\(.*\)\s*\n?\{\s*(?:.|\n)+break;\s*\n\s*(?:default:)?(?:[^}]|\n)*\})"
CASE_PATTERN1 = "(?P<spaces>\s*)case (?P<testvar>\S+) is (?P<testvalue>\S+):"
CASE_PATTERN2 = "(?P<spaces>\s*)case (?P<testvalue>\S+):"
INDENT_SIZE = 3

def processCaseBlock(block, case_pattern, testvar=None):
    blockLines = block.split("\n")
    resLines = []
    tab_size = ""
    firstCase = True
    switchFound = False
    for line in blockLines:
        if not switchFound and "switch" in line:
            switchFound = True
            continue
        if "{" in line:
            continue
        if "}" in line:
            continue
        m = re.match(case_pattern, line)
        if m:
            if not firstCase:
                tab_size = m.group("spaces")
            else:
                tab_size = ""
            op = "if" if firstCase else "elif"
            if firstCase:
                firstCase = False
            if case_pattern == CASE_PATTERN1:
                if firstCase:
                    resLines.append(tab_size + f"{op} isinstance({m.group('testvar')}, {m.group('testvalue')}):")
                else:
                    resLines.append(tab_size[INDENT_SIZE:] + f"{op} isinstance({m.group('testvar')}, {m.group('testvalue')}):")
            elif case_pattern == CASE_PATTERN2:
                if firstCase:
                    resLines.append(tab_size + f"{op} {testvar} == {m.group('testvalue')}:")
                else:
                    resLines.append(tab_size[INDENT_SIZE:] + f"{op} {testvar} == {m.group('testvalue')}:")
            continue
        if "break;" in line:
            continue
        if "default:" in line:
            resLines.append(tab_size + "else:")
            continue
        resLines.append(line)
    return "\n".join(resLines)


def processSwitchCases(code):
    switch_cases = re.findall(SWITCH_CASE_PATTERN, code, flags=re.M)
    while switch_cases:
        for switch_case in switch_cases:
            m = re.match("switch\((?P<testvar>\S+)\)", switch_case)
            testvar = m.group("testvar")
            if testvar == "true":
                processedSwitchCase = processCaseBlock(switch_case, CASE_PATTERN1)
            else:
                processedSwitchCase = processCaseBlock(switch_case, CASE_PATTERN2, testvar)
            code = code.replace(switch_case, processedSwitchCase)
        switch_cases = re.findall(SWITCH_CASE_PATTERN, code, flags=re.M)
    return code


def processCompressedIfELse(line):
    m = re.fullmatch("(?P<leftSide>[^=]* = )(?P<content>.*)", line)
    if m:
        leftSide = m.group("leftSide")
        content = m.group("content")
    else:
        content = line
        leftSide = ""
    i = content.find("?")
    if i == -1:
        return line
    else:
        j = content.rfind(":")
        return leftSide + processCompressedIfELse(content[i+1:j]) + "if " + content[:i] + "else" + content[j+1:]


def processCompressedIfELseInAllCode(code):
    codeLines = code.split("\n")
    regex = r"(.*) \? (.*) : (.*)"
    r = []
    for line in codeLines:
        m = re.match(regex, line)
        if m:
            r.append(processCompressedIfELse(line))
        else:
            r.append(line)
    return "\n".join(r)


def deleteFirstTwoSpaces(code):
    lines = code.split("\n")
    r = []
    for line in lines:
        if line.startswith("  "):
            line = line[INDENT_SIZE:]
        r.append(line)
    return "\n".join(r)


def handleIndent(code):
    lines = code.split("\n")
    r = []
    indentSize = None
    inClass = False
    for i, line in enumerate(lines):
        if not inClass:
            reg = r"(?P<left>.*)class\s*(?P<name>\S+).*"
            inClass = re.match(reg, line)
            if inClass:
                if not indentSize:
                    indentSize = 0
                    for c in lines[i + 2]:
                        if c == " ":
                            indentSize += 1
                        elif c == "\n":
                            indentSize = 0
                            break
                        else:
                            break
                    print("detected indent size:", indentSize)
                inClass = True
        else:
            spaceCount = sum(1 for _ in itertools.takewhile(str.isspace, line))
            line = (spaceCount // indentSize) * INDENT_SIZE * ' ' + line[spaceCount:]
        r.append(line)
    return "\n".join(r)


def handleClassHeader(code):
    lines = code.split("\n")
    r = []
    for line in lines:
        reg = r"(?P<left>.*)class (?P<name>\S+)(?P<parents>.*)"
        m = re.match(reg, line)
        if m:
            parents = m.group("parents").split(" ")
            parents = [p for p in parents if p != "" and p not in ["extends", "implements"]]
            parents = f"({', '.join(parents)})" if len(parents) > 0 else ""
            line = f"{m.group('left')}class {m.group('name')}{parents}:"
        r.append(line)
    return "\n".join(r)


def parseFolderFiles(in_dir, out_dir):
    for f in tqdm(pathlib.Path(in_dir).glob("**/*.as")):
        parseFile(f, pathlib.Path(out_dir) / f.relative_to(in_dir).name.replace(".as", ".py"))


def getLineIndent(line):
    return sum(1 for _ in itertools.takewhile(str.isspace, line))


def postSwitchCaseProcess(code):
    codeLines = code.split("\n")
    testvar  = None
    res = []
    blockIndent = None
    for line in codeLines:

        m = re.match('(\s*)case\s+(\S+)\s+is\s+(.*)\s*\:\s*\n?', line)
        if m:
            blockIndent = m.group(1)[INDENT_SIZE:]
            line = f"{blockIndent}if isinstance({m.group(2)}, {m.group(3)}):"
            res.append(line)
            continue

        m = re.match("(\s*)case\s+(\S+)\s*:\s*\n?", line, flags=re.M)
        if m:
            blockIndent = m.group(1)[INDENT_SIZE:]
            line = f"{blockIndent}if {testvar}  == {m.group(2)}:"
            res.append(line)
            continue

        m = re.match(r"\s*switch\((?P<testvar>\S+)\)", line)
        if m:
            testvar = m.group("testvar")
            continue
        
        m = re.match(r"\s*default\s*:\s*\n?", line)
        if m:
            line = f"{blockIndent}else:"
            res.append(line)
            continue
        if "break" in line:
            continue

        res.append(line)
    return "\n".join(res)


def parseFile(file_p, out_p):
    with open(file_p, "r", encoding="utf8") as fp:
        code = fp.read()
        code = handleClassHeader(code)
        # code = processCompressedIfELseInAllCode(code)
        # code = processSwitchCases(code)
        for pattern, repl in patterns.items():
            code = re.sub(pattern, repl, code, flags=re.MULTILINE)
        code = deleteFirstTwoSpaces(code)
        code = handleIndent(code)
        code = postSwitchCaseProcess(code)
    with open(out_p, "w") as fp:
        fp.write(code)


ROOTDIR = pathlib.Path(os.path.dirname(__file__))
# parseFolderFiles("AS3ToPythonConverter/scripts", "AS3ToPythonConverter/connectionType")
t = perf_counter()
parseFile(ROOTDIR / "target.as", ROOTDIR / "EffectZone.py")
print("parsing took:", perf_counter() - t)
