from com.ankamagames.dofus.network.messages.game.alliance.AllianceJoinedMessage import AllianceJoinedMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.AllianceInformations import AllianceInformations
    


class AllianceMembershipMessage(AllianceJoinedMessage):
    

    def init(self, allianceInfo:'AllianceInformations', enabled:bool, leadingGuildId:int):
        
        super().__init__(allianceInfo, enabled, leadingGuildId)
    
    