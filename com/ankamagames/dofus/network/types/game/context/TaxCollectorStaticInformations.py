from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.GuildInformations import GuildInformations
    


class TaxCollectorStaticInformations(NetworkMessage):
    firstNameId:int
    lastNameId:int
    guildIdentity:'GuildInformations'
    callerId:int
    

    def init(self, firstNameId:int, lastNameId:int, guildIdentity:'GuildInformations', callerId:int):
        self.firstNameId = firstNameId
        self.lastNameId = lastNameId
        self.guildIdentity = guildIdentity
        self.callerId = callerId
        
        super().__init__()
    
    