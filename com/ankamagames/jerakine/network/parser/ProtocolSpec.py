import json
import os
ROOTDIR = os.path.dirname(__file__)
protocol_spec_p = os.path.join(ROOTDIR, "d2protocol.json")
if not os.path.exists(protocol_spec_p):
    raise Exception(f"{protocol_spec_p} file not found")
with open(protocol_spec_p, "r") as fp:
    D2PROTOCOL = json.load(fp)


class ProtocolSpec:
    
    @staticmethod
    def getTypeSpecById(id):
        if str(id) not in D2PROTOCOL["type_by_id"]:
            raise Exception(f"Type id {id} not found in known types ids")
        return D2PROTOCOL["type_by_id"][str(id)]
    
    staticmethod
    def getClassSpecById(id):
        if str(id) not in D2PROTOCOL["msg_by_id"]:
            raise Exception(f"msg id {id} not found in known msg ids")
        return D2PROTOCOL["msg_by_id"][str(id)]
    
    @staticmethod
    def getClassSpecByName(name):
        return D2PROTOCOL["type"][name]
