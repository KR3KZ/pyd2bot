from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class HaapiValidationRequestMessage(NetworkMessage):
    transaction:str
    

    def init(self, transaction:str):
        self.transaction = transaction
        
        super().__init__()
    
    