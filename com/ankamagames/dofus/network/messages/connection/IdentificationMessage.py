from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.version.Version import Version


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
    
    
