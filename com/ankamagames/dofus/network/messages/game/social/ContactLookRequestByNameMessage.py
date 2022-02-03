from com.ankamagames.dofus.network.messages.game.social.ContactLookRequestMessage import ContactLookRequestMessage


class ContactLookRequestByNameMessage(ContactLookRequestMessage):
    playerName:str
    

    def init(self, playerName:str, requestId:int, contactType:int):
        self.playerName = playerName
        
        super().__init__(requestId, contactType)
    
    