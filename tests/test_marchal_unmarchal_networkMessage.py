
from dataclasses import dataclass
from time import perf_counter
from com.ankamagames.dofus.network.messages.connection.IdentificationMessage import IdentificationMessage
from com.ankamagames.dofus.network.messages.security.ClientKeyMessage import ClientKeyMessage
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from pymarshaler.marshal import Marshal
import json

@dataclass
class Version(NetworkMessage):
    major:int
    minor:int
    code:int
    build:int
    buildType:int

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

marshal = Marshal()
result:IdentificationMessage = marshal.unmarshal(IdentificationMessage, imsg)
ckm = ClientKeyMessage(key="fkjdhsfkljh")
print(ckm.key)
print(marshal.marshal(ckm))