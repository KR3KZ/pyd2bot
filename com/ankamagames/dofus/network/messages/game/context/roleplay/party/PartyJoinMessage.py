from com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyMessage import AbstractPartyMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.party.PartyMemberInformations import PartyMemberInformations
    from com.ankamagames.dofus.network.types.game.context.roleplay.party.PartyGuestInformations import PartyGuestInformations
    


class PartyJoinMessage(AbstractPartyMessage):
    partyType:int
    partyLeaderId:int
    maxParticipants:int
    members:list['PartyMemberInformations']
    guests:list['PartyGuestInformations']
    restricted:bool
    partyName:str
    

    def init(self, partyType:int, partyLeaderId:int, maxParticipants:int, members:list['PartyMemberInformations'], guests:list['PartyGuestInformations'], restricted:bool, partyName:str, partyId:int):
        self.partyType = partyType
        self.partyLeaderId = partyLeaderId
        self.maxParticipants = maxParticipants
        self.members = members
        self.guests = guests
        self.restricted = restricted
        self.partyName = partyName
        
        super().__init__(partyId)
    
    