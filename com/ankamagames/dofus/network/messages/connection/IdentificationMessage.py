from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.version.Version import Version


@dataclass
class IdentificationMessage(NetworkMessage):
    version:Version
    lang:str
    credentials:list[int]
    serverId:int
    sessionOptionalSalt:int
    failedAttempts:list[int]
    autoconnect:bool
    useCertificate:bool
    useLoginToken:bool
    
    def __post_init__(self):
        super().__init__()

   