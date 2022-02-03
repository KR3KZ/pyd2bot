from com.ankamagames.dofus.network.messages.connection.IdentificationMessage import IdentificationMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.version.Version import Version
    


class IdentificationAccountForceMessage(IdentificationMessage):
    forcedAccountLogin:str
    

    def init(self, forcedAccountLogin:str, version:'Version', lang:str, credentials:list[int], serverId:int, sessionOptionalSalt:int, failedAttempts:list[int]):
        self.forcedAccountLogin = forcedAccountLogin
        
        super().__init__(version, lang, credentials, serverId, sessionOptionalSalt, failedAttempts)
    
    