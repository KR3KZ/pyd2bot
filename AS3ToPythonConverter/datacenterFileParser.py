
from pathlib import Path
import re
from traceback import print_tb

from jinja2 import Template

CLASS_PATTERN = r"\s*public class (?P<name>\w+) (?:extends (?P<parent>\w+) )?implements (?P<interface>\w+)\n"
PUBLIC_VAR_PATTERN = r"\s*public var (?P<name>\w+):(?P<type>\S*)( = (?P<init>.*))?;\n"
VECTOR_TYPE_PATTERN = r"Vector\.<(?P<type>\w+)>"
MODULE_PATTERN = r'\s*public static const MODULE:String = "(?P<name>\S+)";\n'
OBJECT_BYID_GETTER_PATTERN = r"^\s*public static function get(\S+)ById\(id:int\)\s*\:\s*(\S+)\n\s*\{\n\s*return\s*GameData\.getObject\(\s*MODULE\s*,\s*id\s*\)\s*as\s*(\S+);\n\s*\}\n?$$"
OBJECTS_GETTER_PATTERN = r"\s*public static function get(\S+)\(\)\s*:\s*Array\n?\s*\{\n\s*return\s*GameData\.getObjects\(MODULE\);\n\s*\}\n?"

TO_PTYPE = {
    "Array": "list",
    "Boolean": "bool",
    "Float": "float",
    "Number": "int",
    "uint": "int",
    "String": "str",
    "ByteArray": "bytearray",
}

def parseDofusDCFile(path_to_file):
    parsed = {
        "name": None,
        "parent": None,
        "interface": None,
        "fields": [],
        "module": None,
        "hasGetObjects": None,
        "hasGetObjectById": None,
    }
    with open(path_to_file, "r") as fp:
        match = re.findall(OBJECTS_GETTER_PATTERN, fp.read(), flags=re.MULTILINE)
        if match:
            parsed["hasGetObjects"] = True
        fp.seek(0)
        match = re.findall(OBJECT_BYID_GETTER_PATTERN, fp.read(), flags=re.MULTILINE)
        if match:
            parsed["hasGetObjectById"] = True
        fp.seek(0)
        lines = fp.readlines()
        for line in lines:

            if not parsed["name"]:
                match = re.match(CLASS_PATTERN, line)
                if match:
                    parsed["name"] = match.group("name")
                    parsed["parent"] = match.group("parent")
                    parsed["interface"] = match.group("interface")
            m = re.fullmatch(PUBLIC_VAR_PATTERN, line)
            if m:
                name = m.group("name")
                type = m.group("type")
                init = m.group("init")
                init = None
                if re.fullmatch(VECTOR_TYPE_PATTERN, type):
                    type = type.replace("Vector.", "list")
                    type = type.replace("<", "[")
                    type = type.replace(">", "]")
                for k, v in TO_PTYPE.items():
                    if k in type:
                        type = type.replace(k, v)
                field = {
                    "name": name,
                    "type": type,
                    "init": init
                }
                parsed["fields"].append(field) 

            m = re.fullmatch(MODULE_PATTERN, line)
            if m:
                moduleName = m.group("name")
                parsed["module"] = moduleName

    return parsed

if __name__ == "__main__":
    path_to_folder = r"scripts/AS3ToPythonConverter/alignments"        
    with open("scripts/AS3ToPythonConverter/datacentermodule.j2", "r") as fp:
        template = Template(fp.read())
        for as_file_path in Path(path_to_folder).glob("**/*.as"):
            print("hey")
            parsed = parseDofusDCFile(as_file_path)
            r = template.render(cls=parsed)
            with open(f"scripts/AS3ToPythonConverter/result/{parsed['name']}.py", "w") as fp:
                fp.write(r)