from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeStartOkMulticraftCustomerMessage(NetworkMessage):
    skillId:int
    crafterJobLevel:int
    

    def init(self, skillId:int, crafterJobLevel:int):
        self.skillId = skillId
        self.crafterJobLevel = crafterJobLevel
        
        super().__init__()
    
    