import re
from pathlib import Path
import sys
from tqdm import tqdm
from com.ankamagames.jerakine.network.parser.TypeEnum import TypeEnum
from pathlib import Path
import json
import os
import com.ankamagames.dofus.Constants as Constants

TO_PTYPE = {
    "Array": "list",
    "Boolean": "bool",
    "Float": "float",
    "Number": "int",
    "uint": "int",
    "String": "str",
    "ByteArray": "bytearray",
}


class ProtocolParser:
    CLASS_PATTERN = r"\s*public class (?P<name>\w+) (?:extends (?P<parent>\w+) )?implements (?P<interface>\w+)\n"
    ID_PATTERN = r"\s*public static const protocolId:uint = (?P<id>\d+);\n"
    PUBLIC_VAR_PATTERN = (
        r"\s*public var (?P<name>\w+):(?P<type>\S*)( = (?P<init>.*))?;\n"
    )
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
    WRAPPED_BOOLEAN_PATTERN = (
        r"\s*this.(?P<name>\w+) = BooleanByteWrapper\.getFlag\(.*;\n"
    )

    json = {"type": {}, "msg_by_id": {}, "type_by_id": {}}

    def run(self, src_paths):
        self.getMsgTypesFromSrcs(src_paths)
        for msg_type in tqdm(self.json["type"].values()):
            self.parseMsgType(msg_type)
        self.json["primitives"] = list(
            {
                v["type"]
                for t in self.json["type"].values()
                for v in t["fields"]
                if v["type"] and not v["type"] in self.json["type"]
            }
        )
        return self.json

    def getMsgTypesFromSrcs(self, src_paths):
        for path in src_paths:
            msg_type = {}
            for as_file_path in Path(path).glob("**/*.as"):
                name = as_file_path.name[:-3]
                msg_type[name] = {
                    "name": name,
                    "path": as_file_path,
                    "package": ".".join(
                        as_file_path.parts[as_file_path.parts.index("com") : -1]
                        + (name,)
                    ),
                }
            self.json["type"].update(msg_type)

    def parseVar(self, name, typename, lines):
        var_type = None
        dynamicType = False

        if typename in ["Boolean", "ByteArray"]:
            return {
                "name": name,
                "type": typename,
                "typeId": TypeEnum.fromString(typename).value,
                "lengthTypeId": None,
                "typename": TO_PTYPE.get(typename),
                "optional": False,
                "length": None,
                "dynamicType": False,
            }

        if typename in self.json["type"]:
            var_type = typename

        m = re.fullmatch(self.VECTOR_TYPE_PATTERN, typename)
        if m:
            return self.parseVectorVar(name, m.group("type"), lines)

        attr_assign_pattern = self.ATTR_ASSIGN_PATTERN_OF_NAME % name
        dynamic_type_pattern = self.DYNAMIC_TYPE_PATTERN_OF_TYPE % typename
        optional_var_pattern = self.OPTIONAL_VAR_PATTERN_OF_NAME % name

        optional = False

        for line in lines:
            m = re.fullmatch(attr_assign_pattern, line)
            if m:
                var_type = m.group("type")

            m = re.fullmatch(dynamic_type_pattern, line)
            if m:
                dynamicType = True
                var_type = None

            m = re.fullmatch(optional_var_pattern, line)
            if m:
                optional = True

        if var_type is None and not dynamicType:
            raise Exception(
                f"Unable to parse 'var_type' of attrib {name} from class_type {typename}"
            )

        return {
            "name": name,
            "length": None,
            "type": var_type,
            "dynamicType": dynamicType,
            "typeId": TypeEnum.fromString(var_type).value,
            "lengthTypeId": None,
            "typename": TO_PTYPE.get(typename, typename),
            "optional": optional,
        }

    def parseVectorVar(self, name, typename, lines):
        var_type = None
        dynamicType = False

        if typename in self.json["type"]:
            var_type = typename

        vector_attr_write_pattern = self.VECTOR_ATTR_WRITE_PATTERN_OF_NAME % name
        vector_len_write_pattern = self.VECTOR_LEN_WRITE_PATTERN_OF_NAME % name
        vector_const_len_pattern = self.VECTOR_CONST_LEN_PATTERN_OF_NAME_AND_TYPE % (
            name,
            typename,
        )
        dynamic_type_pattern = self.DYNAMIC_TYPE_PATTERN_OF_TYPE % typename
        lengthType = None
        length = None
        for line in lines:
            m = re.fullmatch(vector_attr_write_pattern, line)
            if m:
                var_type = m.group("type")

            m = re.fullmatch(dynamic_type_pattern, line)
            if m:
                dynamicType = True
                var_type = None

            m = re.fullmatch(vector_len_write_pattern, line)
            if m:
                lengthType = m.group("type")

            m = re.fullmatch(vector_const_len_pattern, line)
            if m:
                length = int(m.group("size"))

        return dict(
            {
                "name": name,
                "length": length,
                "dynamicType": dynamicType,
                "lengthTypeId": TypeEnum.fromString(lengthType).value,
                "type": var_type,
                "typeId": TypeEnum.fromString(var_type).value,
                "typename": TO_PTYPE[typename] if typename in TO_PTYPE else typename,
                "optional": False,
            }
        )

    def parseMsgType(self, msg_type):
        fields = []
        hash_function = False
        wrapped_booleans = set()
        protocolId = None
        if not os.path.exists(msg_type["path"]):
            raise Exception(f"{msg_type['path']} does not exist")
        with open(msg_type["path"], "r") as fp:
            lines = list(fp.readlines())
            msg_type["parent"] = None

            for line in lines:
                m = re.fullmatch(self.CLASS_PATTERN, line)
                if m:
                    assert m.group("name") == msg_type["name"]
                    parent = m.group("parent")
                    if not self.json["type"].get(parent):
                        parent = None
                    msg_type["parent"] = parent

                m = re.fullmatch(self.ID_PATTERN, line)
                if m:
                    protocolId = int(m.group("id"))

                m = re.fullmatch(self.PUBLIC_VAR_PATTERN, line)
                if m:
                    var = self.parseVar(m.group("name"), m.group("type"), lines)
                    fields.append(var)

                m = re.fullmatch(self.HASH_FUNCTION_PATTERN, line)
                if m:
                    hash_function = True

                m = re.fullmatch(self.WRAPPED_BOOLEAN_PATTERN, line)
                if m:
                    wrapped_booleans.add(m.group("name"))
        if protocolId is None:
            raise Exception(f"{msg_type['path']} does not have protocolId")
        msg_type["protocolId"] = protocolId

        if "messages" in str(msg_type["path"]):
            assert protocolId not in self.json["msg_by_id"]
            self.json["msg_by_id"][protocolId] = msg_type

        elif "types" in str(msg_type["path"]):
            assert protocolId not in self.json["type_by_id"]
            self.json["type_by_id"][protocolId] = msg_type

        if sum(field["type"] == "Boolean" for field in fields) > 1:
            boolfields = [var for var in fields if var["name"] in wrapped_booleans]
            fields = [var for var in fields if var["name"] not in wrapped_booleans]

        else:
            boolfields = []

        msg_type["fields"] = list(fields)
        msg_type["boolfields"] = list(boolfields)
        msg_type["hash_function"] = hash_function
        del msg_type["path"]


def parseVersion(metaDataAs):
    PROTOCOL_BUILD_REGX = (
        '^\s*public static const PROTOCOL_BUILD:String = "(?P<protocol_build>.*)";'
    )
    PROTOCOL_DATE_REGX = (
        '^\s*public static const PROTOCOL_DATE:String = "(?P<protocol_date>.*)";'
    )
    with open(metaDataAs, "r") as fp:
        lines = list(fp.readlines())
        for line in lines:
            m = re.match(PROTOCOL_BUILD_REGX, line)
            if m:
                build = m.group("protocol_build")
            else:
                m = re.match(PROTOCOL_DATE_REGX, line)
                if m:
                    date = m.group("protocol_date")
    return build, date


if __name__ == "__main__":
    src_dir = Path(sys.argv[1])

    src_paths = [
        src_dir / "scripts/com/ankamagames/dofus/network/types",
        src_dir / "scripts/com/ankamagames/dofus/network/messages",
    ]
    protocol_json = {}
    version, date = parseVersion(
        src_dir / "scripts/com/ankamagames/dofus/network/Metadata.as"
    )
    protocol_json["version"] = version
    protocol_json["date"] = date

    protocol_json.update(ProtocolParser().run(src_paths))

    with open(Constants.PROTOCOL_SPEC_PATH, "w") as fp:
        json.dump(protocol_json, fp, indent=4, separators=(", ", ": "), sort_keys=True)
