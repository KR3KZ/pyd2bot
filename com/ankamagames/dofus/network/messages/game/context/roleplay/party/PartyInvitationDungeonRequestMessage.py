from com.ankamagames.dofus.network.messages.game.context.roleplay.party.PartyInvitationRequestMessage import PartyInvitationRequestMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.common.AbstractPlayerSearchInformation import AbstractPlayerSearchInformation
    


class PartyInvitationDungeonRequestMessage(PartyInvitationRequestMessage):
    dungeonId:int
    

    def init(self, dungeonId:int, target:'AbstractPlayerSearchInformation'):
        self.dungeonId = dungeonId
        
        super().__init__(target)
    
    