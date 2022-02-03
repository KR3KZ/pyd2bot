from com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyMessage import AbstractPartyMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.party.PartyInvitationMemberInformations import PartyInvitationMemberInformations
    from com.ankamagames.dofus.network.types.game.context.roleplay.party.PartyGuestInformations import PartyGuestInformations
    


class PartyInvitationDetailsMessage(AbstractPartyMessage):
    partyType:int
    partyName:str
    fromId:int
    fromName:str
    leaderId:int
    members:list['PartyInvitationMemberInformations']
    guests:list['PartyGuestInformations']
    

    def init(self, partyType:int, partyName:str, fromId:int, fromName:str, leaderId:int, members:list['PartyInvitationMemberInformations'], guests:list['PartyGuestInformations'], partyId:int):
        self.partyType = partyType
        self.partyName = partyName
        self.fromId = fromId
        self.fromName = fromName
        self.leaderId = leaderId
        self.members = members
        self.guests = guests
        
        super().__init__(partyId)
    
    