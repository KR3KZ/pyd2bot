from com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyMessage import AbstractPartyMessage


class PartyInvitationCancelledForGuestMessage(AbstractPartyMessage):
    cancelerId:int
    

    def init(self, cancelerId:int, partyId:int):
        self.cancelerId = cancelerId
        
        super().__init__(partyId)
    
    