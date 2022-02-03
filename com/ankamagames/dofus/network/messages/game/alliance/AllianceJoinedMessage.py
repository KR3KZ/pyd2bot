from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.AllianceInformations import AllianceInformations
    


class AllianceJoinedMessage(NetworkMessage):
    allianceInfo:'AllianceInformations'
    enabled:bool
    leadingGuildId:int
    

    def init(self, allianceInfo:'AllianceInformations', enabled:bool, leadingGuildId:int):
        self.allianceInfo = allianceInfo
        self.enabled = enabled
        self.leadingGuildId = leadingGuildId
        
        super().__init__()
    
    