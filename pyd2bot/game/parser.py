import re


patterns = {

    "package \S+\n?": "",
    "import \S+\n?": "",
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

    " (?:implements|extends) (\S+)": r"(\1)",
    "class(.*)": r"class\1:",

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

    "_log:Logger = Log\.getLogger\((.*)\)": r'logger = logging.getLogger("bot")',
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
    ".getInstance()": "",
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
}

with open("pyd2bot/game/target.as", "r") as fp:
    code = fp.read()
    for pattern, repl in patterns.items():
            code = re.sub(pattern, repl, code, flags=re.M)

with open("pyd2bot/gameData/monster.py", "w") as fp:
    fp.write(code)

