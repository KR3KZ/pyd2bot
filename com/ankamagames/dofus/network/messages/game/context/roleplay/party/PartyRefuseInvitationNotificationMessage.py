from com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyEventMessage import AbstractPartyEventMessage


class PartyRefuseInvitationNotificationMessage(AbstractPartyEventMessage):
    guestId:int
    

    def init(self, guestId:int, partyId:int):
        self.guestId = guestId
        
        super().__init__(partyId)
    
    