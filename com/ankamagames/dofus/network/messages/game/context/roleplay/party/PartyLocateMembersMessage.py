from com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyMessage import AbstractPartyMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.party.PartyMemberGeoPosition import PartyMemberGeoPosition
    


class PartyLocateMembersMessage(AbstractPartyMessage):
    geopositions:list['PartyMemberGeoPosition']
    

    def init(self, geopositions:list['PartyMemberGeoPosition'], partyId:int):
        self.geopositions = geopositions
        
        super().__init__(partyId)
    
    