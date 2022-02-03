from com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyMessage import AbstractPartyMessage


class PartyCancelInvitationMessage(AbstractPartyMessage):
    guestId:int
    

    def init(self, guestId:int, partyId:int):
        self.guestId = guestId
        
        super().__init__(partyId)
    
    