from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class HaapiConfirmationMessage(NetworkMessage):
    kamas:int
    amount:int
    rate:int
    action:int
    transaction:str
    

    def init(self, kamas:int, amount:int, rate:int, action:int, transaction:str):
        self.kamas = kamas
        self.amount = amount
        self.rate = rate
        self.action = action
        self.transaction = transaction
        
        super().__init__()
    
    