from com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyEventMessage import AbstractPartyEventMessage


class PartyCancelInvitationNotificationMessage(AbstractPartyEventMessage):
    cancelerId:int
    guestId:int
    

    def init(self, cancelerId:int, guestId:int, partyId:int):
        self.cancelerId = cancelerId
        self.guestId = guestId
        
        super().__init__(partyId)
    
    