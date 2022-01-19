import re
from pathlib import Path
from tqdm import tqdm

class ProtocolParser:
    CLASS_PATTERN = r"\s*public class (?P<name>\w+) (?:extends (?P<parent>\w+) )?implements (?P<interface>\w+)\n"
    ID_PATTERN = r"\s*public static const protocolId:uint = (?P<id>\d+);\n"
    PUBLIC_VAR_PATTERN = r"\s*public var (?P<name>\w+):(?P<type>\S*)( = (?P<init>.*))?;\n"
    VECTOR_TYPE_PATTERN = r"Vector\.<(?P<type>\w+)>"

    ATTR_ASSIGN_PATTERN_OF_NAME = r"\s*this\.%s = (?:\w*)\.read(?P<type>\w*)\(\);\n"
    VECTOR_ATTR_WRITE_PATTERN_OF_NAME = (
        r"\s*(?:\w*)\.write(?P<type>\w*)\(this\.%s\[(?:\w+)\]\);\n"
    )
    VECTOR_LEN_WRITE_PATTERN_OF_NAME = (
        r"\s*(?:\w*)\.write(?P<type>\w*)\(this\.%s\.length\);\n"
    )
    VECTOR_CONST_LEN_PATTERN_OF_NAME_AND_TYPE = (
        r"\s*this\.%s = new Vector\.<%s>\((?P<size>\d+),true\);\n"
    )
    DYNAMIC_TYPE_PATTERN_OF_TYPE = (
        r"\s*(?:this\.)?\w+ = ProtocolTypeManager\.getInstance\(%s,\w*\);\n"
    )
    OPTIONAL_VAR_PATTERN_OF_NAME = r"\s*if\(this\.%s == null\)\n"
    HASH_FUNCTION_PATTERN = r"\s*HASH_FUNCTION\(data\);\n"
    WRAPPED_BOOLEAN_PATTERN = r"\s*this.(?P<name>\w+) = BooleanByteWrapper\.getFlag\(.*;\n"
    
    def __init__(self):
        self.json = {
            "type": {},
            "msg_by_id": {},
            "type_by_id": {}
        }
    
    def run(self, src_paths):
        self.getMsgTypesFromSrcs(src_paths)
        for msg_type in tqdm(self.json["type"].values()):
            self.parseMsgType(msg_type)
        self.json["primitives"] = list({
            v["type"]
            for t in self.json["type"].values()
            for v in t["vars"]
            if v["type"] and not v["type"] in self.json["type"]
        })
        return self.json
        
    def getMsgTypesFromSrcs(self, src_paths):
        for path in src_paths:
            msg_type = {}
            for as_file_path in Path(path).glob("**/*.as"):
                name = as_file_path.name[:-3]
                msg_type[name] = {
                    "name": name,
                    "path": as_file_path
                }
            self.json["type"].update(msg_type)
    
    def parseVar(self, name, type_name, lines):
        var_type = None
        if type_name in ["Boolean", "ByteArray"]:
            return dict(name=name, length=None, type=type_name, optional=False)
        if type_name in self.json["type"]:
            var_type = type_name

        m = re.fullmatch(self.VECTOR_TYPE_PATTERN, type_name)
        if m:
            return self.parseVectorVar(name, m.group("type"), lines)

        attr_assign_pattern = self.ATTR_ASSIGN_PATTERN_OF_NAME % name
        dynamic_type_pattern = self.DYNAMIC_TYPE_PATTERN_OF_TYPE % type_name
        optional_var_pattern = self.OPTIONAL_VAR_PATTERN_OF_NAME % name

        optional = False

        for line in lines:
            m = re.fullmatch(attr_assign_pattern, line)
            if m:
                var_type = m.group("type")

            m = re.fullmatch(dynamic_type_pattern, line)
            if m:
                var_type = False

            m = re.fullmatch(optional_var_pattern, line)
            if m:
                optional = True
        if var_type is None:
            raise Exception(f"Unable to parse 'var_type' of attrib {name} from class_type {type_name}")
        
        return {
            "name": name,
            "length": None,
            "type": var_type,
            "optional": optional
        }

    def parseVectorVar(self, name, typename, lines):
        if typename in self.json["type"]:
            type = typename

        vector_attr_write_pattern = self.VECTOR_ATTR_WRITE_PATTERN_OF_NAME % name
        vector_len_write_pattern = self.VECTOR_LEN_WRITE_PATTERN_OF_NAME % name
        vector_const_len_pattern = self.VECTOR_CONST_LEN_PATTERN_OF_NAME_AND_TYPE % (
            name,
            typename,
        )
        dynamic_type_pattern = self.DYNAMIC_TYPE_PATTERN_OF_TYPE % typename

        for line in lines:
            m = re.fullmatch(vector_attr_write_pattern, line)
            if m:
                type = m.group("type")

            m = re.fullmatch(dynamic_type_pattern, line)
            if m:
                type = False

            m = re.fullmatch(vector_len_write_pattern, line)
            if m:
                length = m.group("type")

            m = re.fullmatch(vector_const_len_pattern, line)
            if m:
                length = int(m.group("size"))

        return dict(name=name, length=length, type=type, optional=False)

    def parseMsgType(self, msg_type):
        vars = []
        hash_function = False
        wrapped_booleans = set()

        with open(msg_type["path"], 'r') as fp:
            lines = list(fp.readlines())
            for line in lines:
                m = re.fullmatch(self.CLASS_PATTERN, line)
                if m:
                    assert m.group("name") == msg_type["name"]
                    parent = m.group("parent")
                    if parent not in self.json["type"]:
                        parent = None
                    msg_type["parent"] = parent

                m = re.fullmatch(self.ID_PATTERN, line)
                if m:
                    protocolId = int(m.group("id"))

                m = re.fullmatch(self.PUBLIC_VAR_PATTERN, line)
                if m:
                    var = self.parseVar(m.group("name"), m.group("type"), lines)
                    vars.append(var)

                m = re.fullmatch(self.HASH_FUNCTION_PATTERN, line)
                if m:
                    hash_function = True

                m = re.fullmatch(self.WRAPPED_BOOLEAN_PATTERN, line)
                if m:
                    wrapped_booleans.add(m.group("name"))

        msg_type["protocolId"] = protocolId

        if "messages" in str(msg_type["path"]):
            assert protocolId not in self.json["msg_by_id"]
            self.json["msg_by_id"][protocolId] = msg_type
            
        elif "types" in str(msg_type["path"]):
            assert protocolId not in self.json["type_by_id"]
            self.json["type_by_id"][protocolId] = msg_type

        if sum(var["type"] == "Boolean" for var in vars) > 1:
            boolVars = [var for var in vars if var["name"] in wrapped_booleans]
            vars = [var for var in vars if var["name"] not in wrapped_booleans]
        else:
            boolVars = []

        msg_type["vars"] = list(vars)
        msg_type["boolVars"] = list(boolVars)
        msg_type["hash_function"] = hash_function
        del msg_type["path"]

