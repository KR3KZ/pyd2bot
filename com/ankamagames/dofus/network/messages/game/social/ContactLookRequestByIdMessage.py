from com.ankamagames.dofus.network.messages.game.social.ContactLookRequestMessage import ContactLookRequestMessage


class ContactLookRequestByIdMessage(ContactLookRequestMessage):
    playerId:int
    

    def init(self, playerId:int, requestId:int, contactType:int):
        self.playerId = playerId
        
        super().__init__(requestId, contactType)
    
    