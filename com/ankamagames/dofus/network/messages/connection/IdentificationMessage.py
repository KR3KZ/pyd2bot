from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.version.Version import Version


class IdentificationMessage(INetworkMessage):
    protocolId = 4337
    version:Version
    lang:str
    credentials:int
    serverId:int
    sessionOptionalSalt:int
    failedAttempts:int
    autoconnect:bool
    useCertificate:bool
    useLoginToken:bool
    
    
