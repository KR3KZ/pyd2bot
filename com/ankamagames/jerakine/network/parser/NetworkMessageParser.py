from functools import reduce
import json
from pathlib import Path
import random
import os
from time import perf_counter
from com.ankamagames.jerakine.network.CustomDataWrapper import ByteArray
from com.ankamagames.jerakine.network.parser.TypeEnum import TypeEnum
ROOTDIR = os.path.dirname(__file__)
D2PROTOCOL_PATH = Path(ROOTDIR) / "d2protocol.json"
D2PROTOCOL = json.load(D2PROTOCOL_PATH.open("r"))
D2PROTOCOL["primitives"] = set(D2PROTOCOL["primitives"])
dataReadWrite = {
    name: (getattr(ByteArray, "read" + name), getattr(ByteArray, "write" + name))
    for name in D2PROTOCOL["primitives"]
}

class NetworkMessageParser:

    def getTypeById(self, id):
        return D2PROTOCOL["type_by_id"][str(id)]

    @classmethod
    def getSpecByName(cls, name):
        return D2PROTOCOL["type"][name]

    @classmethod
    def isPrimitive(cls, name):
        return name in D2PROTOCOL["primitives"]
    
    @classmethod
    def readBooleans(cls, boolfields, data: ByteArray):
        ans = {}
        bfields = iter(boolfields)
        for _ in range(0, len(boolfields), 8):
            bits = format(data.readByte(), "08b")[::-1]
            for val, var in zip(bits, bfields):
                ans[var["name"]] = val == "1"
        return ans

    @classmethod
    def readArray(cls, var, data: ByteArray):
        n = var.get("length")

        if n is None:
            lTypeId = var.get("lengthTypeId")
            primitiveName = TypeEnum.getPrimitiveName(TypeEnum(lTypeId))
            n = dataReadWrite[primitiveName][0](data)

        ans = []
        if var["type"] in D2PROTOCOL["primitives"]:
            for _ in range(n): 
                ans.append(dataReadWrite[var["type"]][0](data))

        else:
            for _ in range(n):
                ans.append(cls.to_json(D2PROTOCOL[var["name"]], data))

        return ans

    @classmethod
    def to_json(cls, spec:dict, data: ByteArray):
        if spec.get("dynamicType"):
            msg_type_id = data.readUnsignedShort()
            msg_type = cls.getTypeById(msg_type_id)
            
        typeId = spec.get("typeId")
        if typeId is not None and TypeEnum(typeId) != TypeEnum.OBJECT:
            return dataReadWrite[spec["type"]][0](data)

        parent = spec.get("parent")
        if parent is not None:
            ans = cls.to_json(D2PROTOCOL["type"]["parent"], data)

        else:
            ans = {}

        if "fields" not in spec:
            spec = D2PROTOCOL["type"][spec["type"]]
            
        ans.update(cls.readBooleans(spec["boolfields"], data))
        
        for field in spec["fields"]:
            
            if field["optional"]:
                if not data.readByte():
                    continue

            if field["length"] is not None or field.get("lengthTypeId") is not None:
                ans[field["name"]] = cls.readArray(field, data)

            else:
                ans[field["name"]] = cls.to_json(field, data)
            
        if spec["hash_function"] and data.remaining() == 48:
            ans["hash_function"] = data.read(48)

        return ans

    @classmethod
    def writeBooleans(cls, boolfields, el, data: ByteArray):
        bits = []
        for var in boolfields:
            bits.append(el[var["name"]])
            if len(bits) == 8:
                data.writeByte(reduce(lambda a, b: 2 * a + b, bits[::-1]))
                bits = []
        if bits:
            data.writeByte(reduce(lambda a, b: 2 * a + b, bits[::-1]))

    @classmethod
    def writeArray(cls, var, el, data):
        n = len(el)
        if var["length"] is not None:
            assert n == var["length"]

        elif var["lengthTypeId"] is not None:
            primitiveName = TypeEnum.getPrimitiveName(TypeEnum(var["lengthTypeId"]))
            dataReadWrite[primitiveName][1](data, n)
        
        if var["type"] in D2PROTOCOL["primitives"]:
            for it in el:
                dataReadWrite[var["type"]][1](data, it)
                
        else:
            for it in el:
                cls.from_json(D2PROTOCOL[var["name"]], it, data)

    @classmethod
    def from_json(cls, spec:dict, json, data=None, random_hash=True) -> ByteArray:
        if data is None:
            data = ByteArray()
            
        if spec.get("dynamicType"):
            msg_type = cls.getSpecByName(spec["name"])
            data.writeUnsignedShort(msg_type["protocolId"])

        typeId = spec.get("typeId")
        if typeId is not None and TypeEnum(typeId) != TypeEnum.OBJECT:
            dataReadWrite[spec["type"]][1](data, json)
            return data
        
        parent = spec.get("parent")
        if parent is not None:
            cls.from_json(D2PROTOCOL["type"][parent], json, data)

        if "fields" not in spec:
            spec = D2PROTOCOL["type"][spec["type"]]

        cls.writeBooleans(spec["boolfields"], json, data)
        for field in spec["fields"]:
            if field["optional"]:
                if field["name"] in json:
                    data.writeByte(1)
                else:
                    data.writeByte(0)
                    continue

            if field["length"] is not None or field.get("lengthTypeId") is not None:
                cls.writeArray(field, json[field["name"]], data)

            else:
                cls.from_json(field, json[field["name"]], data)
                
        if "hash_function" in json:
            data.write(json["hash_function"])
            
        elif spec["hash_function"] and random_hash:
            hash = bytes(random.getrandbits(8) for _ in range(48))
            data.write(hash)
            
        return data


if __name__ == "__main__":
    imsg = {
        'autoconnect': False,
        'credentials': [11, -1],
        'failedAttempts': [],
        'lang': 'fr',
        'serverId': 0,
        'sessionOptionalSalt': 0,
        'useCertificate': False,
        'useLoginToken': False,
        'version': {
            'build': 11,
            'buildType': 0,
            'code': 5,
            'major': 2,
            'minor': 62
        }
    }
    spec = D2PROTOCOL["type"]["IdentificationMessage"]
    bamsg = NetworkMessageParser.from_json(spec, imsg)
    from com.ankamagames.dofus.network.messages.connection.IdentificationMessage import IdentificationMessage

    t = perf_counter()
    imsg1:IdentificationMessage = IdentificationMessage.unpack(bamsg, len(bamsg))
    print("unpack:", perf_counter() - t)

    d = {imsg1.__post_init__(): "3"}
    t = perf_counter()
    bamsg2 = imsg1.pack()
    print("pack:", perf_counter() - t)
    
    bamsg.position = 0
    t = perf_counter()
    imsg1:IdentificationMessage = IdentificationMessage.unpack(bamsg, len(bamsg))
    print("unpack:", perf_counter() - t)

    t = perf_counter()
    bamsg2 = imsg1.pack()
    print("pack:", perf_counter() - t)


    
