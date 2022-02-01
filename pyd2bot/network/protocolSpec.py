from functools import reduce
from importlib import import_module
import random
from com.ankamagames.jerakine.network.CustomDataWrapper import ByteArray
import json
import os
from protocolBuilder.typeEnum import TypeEnum

class UnknownMsgIdError(Exception):
    pass

class UnknownTypeIdError(Exception):
    pass

class ProtocolSpecNotFoundError(Exception):
    pass

ROOTDIR = os.path.dirname(__file__)

class ProtocolSpec:
    protocol_spec_p = os.path.join(ROOTDIR, "spec.json")
    
    if not os.path.exists(protocol_spec_p):
        raise ProtocolSpecNotFoundError(f"{protocol_spec_p} file not found")

    with open(protocol_spec_p, "r") as fp:
        PROTOCOL_SPEC = json.load(fp)
    
    @staticmethod
    def getTypeSpecById(id):
        if str(id) not in ProtocolSpec.PROTOCOL_SPEC["type_by_id"]:
            raise UnknownTypeIdError(f"Type id {id} not found in known types ids")
        return ProtocolSpec.PROTOCOL_SPEC["type_by_id"][str(id)]
    
    staticmethod
    def getClassSpecById(id):
        if str(id) not in ProtocolSpec.PROTOCOL_SPEC["msg_by_id"]:
            raise UnknownMsgIdError(f"msg id {id} not found in known msg ids")
        return ProtocolSpec.PROTOCOL_SPEC["msg_by_id"][str(id)]
    
    @staticmethod
    def getClassSpecByName(name):
        return ProtocolSpec.PROTOCOL_SPEC["type"][name]

    def writeBooleans(self, boolfields, el, raw: ByteArray):
        bits = []
        for var in boolfields:
            bits.append(el[var["name"]])
            if len(bits) == 8:
                raw.writeByte(reduce(lambda a, b: 2 * a + b, bits[::-1]))
                bits = []
        if bits:
            raw.writeByte(reduce(lambda a, b: 2 * a + b, bits[::-1]))

    def writeArray(self, field, el, raw):
        assert field["length"] is not None
        n = len(el)
        if isinstance(field["length"], int):
            assert n == field["length"]
        else:
            self.write(field["length"], n, raw)
        for it in el:
            self.write(field["type"], it, raw)

    def write(self, msgName, json, raw=None, random_hash=True) -> ByteArray:
        if raw is None:
            raw = ByteArray()
            
        if msgName is False:
            msg_type = self.getTypeSpecById[json["type"]]
            raw.writeUnsignedShort(msg_type["protocolId"])
            
        elif isinstance(msgName, str):
            if self.isPrimitive(msgName):
                getattr(ByteArray, "write" + msgName)(raw, json)
                return raw
            msg_type = self.getFieldTypeId(msgName)
            
        parent = msg_type["parent"]
        if parent is not None:
            self.write(parent, json, raw)
            
        self.writeBooleans(msg_type["boolfields"], json, raw)
        for var in msg_type["fields"]:
            if var["optional"]:
                if var["name"] in json:
                    raw.writeByte(1)
                else:
                    raw.writeByte(0)
                    continue
            if var["length"] is not None:
                self.writeArray(var, json[var["name"]], raw)
            else:
                self.write(var["type"], json[var["name"]], raw)
                
        if "hash_function" in json:
            raw.write(json["hash_function"])
            
        elif msg_type["hash_function"] and random_hash:
            hash = bytes(random.getrandbits(8) for _ in range(48))
            raw.write(hash)
            
        return raw
