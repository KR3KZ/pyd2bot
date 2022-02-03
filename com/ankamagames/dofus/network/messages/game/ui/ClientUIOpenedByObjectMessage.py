from com.ankamagames.dofus.network.messages.game.ui.ClientUIOpenedMessage import ClientUIOpenedMessage


class ClientUIOpenedByObjectMessage(ClientUIOpenedMessage):
    uid:int
    

    def init(self, uid:int, type:int):
        self.uid = uid
        
        super().__init__(type)
    
    