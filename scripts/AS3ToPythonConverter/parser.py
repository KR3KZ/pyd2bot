import os
import pathlib
import re
from tqdm import tqdm

patterns = {
    "^\s*from com.ankamagames.jerakine.logger.Log import Log": "",
    "^\s*import com.ankamagames.jerakine.logger.Logger;": "from com.ankamagames.jerakine.logger.Logger import Logger",
    "package \S+\n?": "",

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
    "null": "None",
    "Number": "float",
    "String": "str",
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
    ".push": ".append",
    " (?:implements|extends) (.*)": r"(\1)",
    "^(?:\s*)class ([A-Z]+\S+)": r"class \1:",
    "= (.*) \? (.*) : (.*)": r"= \2 if \1 else \3",
    "(if|elif|else|for|while)\((.*)\)": r"\1 \2:",
    "Vector\.<(\S+)>": r"list[\1]",
    "function (\S+)\((.*)\) : (\S+)": r"def \1(self, \2) -> \3:",
    "function (\S+)\((.*)\) :": r"def \1(self, \2):",
    "if !(.*)": r"if not \1",
    "for each\((\S+) in (\S+)\)": r"for \1 in \2:",
    "(\S+)\.length": r"len(\1)",
    "throw Error(.*)": r"raise Exception\1",
    r'^(.*)function get (\S+)\((.*)\) : (\S+)$': r"\1@property\n\1def \2(self, \3) -> \4:",
    r'^(.*)function set (\S+)\((.*)\) : (\S+)$': r"\1@\2.setter\n\1def \2(self, \3) -> \4:",
    "function [A-Z]+(\S+)\((.*)\)": r"def __init__(self, \2):",
    "\(?(\S+) as (\S+)\)?": r"\1",
    "_log:Logger = Log\.getLogger\((.*)\)": r'logger = Logger(__name__)',
    ", \)": r")",
    "!==": r"is not",
    "!(\w+)": r"not \1",
    "delete ": r"del ",
    "_log.(info|error|debug)\((.*)\)": r"logger.\1(\2)",
    "else$": r"else:",
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
    "(elif|if) (\S+) is ([A-Z]+\S+):": r"\1 isinstance(\2, \3):",
    "super\((.*)\)": r"super().__init__(\1)",
    "super\.": r"super().",
    "(\S+).__str__\(\)": r"str(\1)",
    "for (\S+):(\S+) = (\S+) (\S+) (.*) (\S+) (\S+) (\S+) (\S+):": r"for \1 in range(\3, \6, \9):",
    "Function" : "FunctionType",
    "strUtils.replace\((.*),(.*),(.*)\)": r"str.replace(\1, \2, \3)",
    ".indexOf": ".find",
    "\.substring\((.*?),(.*?)\)": r"[\1:\2]",
    "\.substring\((.*)\)": r"[:\1]",
    " implements IDataCenter": "",
    "catch\(e\:Error\)": "except Exception as e:",
    "catch\(e\:(\S+)\)": r"except \1 as e:",
    "try": "try:",
    "_log": "logger",
    "throw ([A-Z]+\S+)": r"raise \1",
    "IDataInput": "BinaryStream",
    "Object": "object",
    "-> \*": "-> Any",
    "Class": "object",
    ".concat": ".extend",

}

def parseFolderFiles(in_dir, out_dir):
    for f in tqdm(pathlib.Path(in_dir).glob("**/*.as")):
        parseFile(f, pathlib.Path(out_dir) / f.relative_to(in_dir).name.replace(".as", ".py"))

def parseFile(file_p, out_p):
    with open(file_p, "r", encoding="utf8") as fp:
        code = fp.read()
        for pattern, repl in patterns.items():
                code = re.sub(pattern, repl, code, flags=re.M)

    with open(out_p, "w") as fp:
        fp.write(code)

# parseFolderFiles("AS3ToPythonConverter/scripts", "AS3ToPythonConverter/connectionType")
parseFile("scripts/AS3ToPythonConverter/target.as", "scripts/AS3ToPythonConverter/MapPosition.py")
