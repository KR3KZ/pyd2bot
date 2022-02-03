from com.ankamagames.dofus.network.messages.game.context.roleplay.party.PartyUpdateMessage import PartyUpdateMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.party.PartyMemberInformations import PartyMemberInformations
    


class PartyNewMemberMessage(PartyUpdateMessage):
    

    def init(self, memberInformations:'PartyMemberInformations', partyId:int):
        
        super().__init__(memberInformations, partyId)
    
    