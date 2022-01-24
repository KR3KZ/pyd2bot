from functools import reduce
import logging
import random
from pyd2bot.utils.binaryIO.customDataWrapper import ByteArray
import json
import os

class UnknownMsgIdError(Exception):
    pass

class UnknownTypeIdError(Exception):
    pass

class ProtocolSpecNotFoundError(Exception):
    pass

ROOTDIR = os.path.dirname(__file__)

class DofusProtocol:
    protocol_spec_p = os.path.join(ROOTDIR, "protocol_spec.json")
    
    if not os.path.exists(protocol_spec_p):
        raise ProtocolSpecNotFoundError(f"{protocol_spec_p} file not found")
    with open(protocol_spec_p, "r") as fp:
        json = json.load(fp)
    
    def getTypeById(self, id):
        if str(id) not in self.json["type_by_id"]:
            raise UnknownTypeIdError(f"Type id {id} not found in known types ids")
        return self.json["type_by_id"][str(id)]
    
    def getMsgById(self, id):
        if str(id) not in self.json["msg_by_id"]:
            raise UnknownMsgIdError(f"msg id {id} not found in known msg ids")
        return self.json["msg_by_id"][str(id)]
    
    def getMsgTypeByName(self, name):
        return self.json["type"].get(name)

    def isPrimitive(self, name):
        return name in self.json["primitives"]
    
    def readBooleans(self, boolVars, data: ByteArray):
        ans = {}
        bvars = iter(boolVars)
        for _ in range(0, len(boolVars), 8):
            bits = format(data.readByte(), "08b")[::-1]
            for val, var in zip(bits, bvars):
                ans[var["name"]] = val == "1"
        return ans

    def readArray(self, var, data: ByteArray):
        assert var["length"] is not None
        if isinstance(var["length"], int):
            n = var["length"]
        else:
            n = self.read(var["length"], data)
        ans = []
        for _ in range(n):
            ans.append(self.read(var["type"], data))
        return ans

    def read(self, type_name, data: ByteArray):
        if not type_name:
            msg_type_id = data.readUnsignedShort()
            msg_type = self.getTypeById(msg_type_id)
            
        else:
            if self.isPrimitive(type_name):
                return getattr(ByteArray, "read" + type_name)(data)
            msg_type = self.getMsgTypeByName(type_name)

        if msg_type["parent"] is not None:
            ans = self.read(msg_type["parent"], data)
            ans["__type__"] = msg_type["name"]
            
        else:
            ans = {"__type__": msg_type["name"]}

        ans.update(self.readBooleans(msg_type["boolVars"], data))
        

        for var in msg_type["vars"]:
            
            if var["optional"]:
                if not data.readByte():
                    continue
            if var["length"] is not None:
                ans[var["name"]] = self.readArray(var, data)
            else:
                ans[var["name"]] = self.read(var["type"], data)
            
        if msg_type["hash_function"] and data.remaining() == 48:
            ans["hash_function"] = data.read(48)
        return ans

    def writeBooleans(self, boolVars, el, data: ByteArray):
        bits = []
        for var in boolVars:
            bits.append(el[var["name"]])
            if len(bits) == 8:
                data.writeByte(reduce(lambda a, b: 2 * a + b, bits[::-1]))
                bits = []
        if bits:
            data.writeByte(reduce(lambda a, b: 2 * a + b, bits[::-1]))

    def writeArray(self, var, el, data):
        assert var["length"] is not None
        n = len(el)
        if isinstance(var["length"], int):
            assert n == var["length"]
        else:
            self.write(var["length"], n, data)
        for it in el:
            self.write(var["type"], it, data)

    def write(self, msg_type_name, json, data=None, random_hash=True) -> ByteArray:
        if data is None:
            data = ByteArray()
            
        if msg_type_name is False:
            msg_type = self.getMsgTypeByName[json["__type__"]]
            data.writeUnsignedShort(msg_type["protocolId"])
            
        elif isinstance(msg_type_name, str):
            if self.isPrimitive(msg_type_name):
                getattr(ByteArray, "write" + msg_type_name)(data, json)
                return data
            msg_type = self.getMsgTypeByName(msg_type_name)
            
        parent = msg_type["parent"]
        if parent is not None:
            self.write(parent, json, data)
            
        self.writeBooleans(msg_type["boolVars"], json, data)
        for var in msg_type["vars"]:
            if var["optional"]:
                if var["name"] in json:
                    data.writeByte(1)
                else:
                    data.writeByte(0)
                    continue
            if var["length"] is not None:
                self.writeArray(var, json[var["name"]], data)
            else:
                self.write(var["type"], json[var["name"]], data)
                
        if "hash_function" in json:
            data.write(json["hash_function"])
            
        elif msg_type["hash_function"] and random_hash:
            hash = bytes(random.getrandbits(8) for _ in range(48))
            data.write(hash)
            
        return data
