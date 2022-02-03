from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.version.Version import Version
    


class IdentificationMessage(NetworkMessage):
    version:'Version'
    lang:str
    credentials:list[int]
    serverId:int
    sessionOptionalSalt:int
    failedAttempts:list[int]
    autoconnect:bool
    useCertificate:bool
    useLoginToken:bool
    

    def init(self, version:'Version', lang:str, credentials:list[int], serverId:int, sessionOptionalSalt:int, failedAttempts:list[int]):
        self.version = version
        self.lang = lang
        self.credentials = credentials
        self.serverId = serverId
        self.sessionOptionalSalt = sessionOptionalSalt
        self.failedAttempts = failedAttempts
        
        super().__init__()
    
    