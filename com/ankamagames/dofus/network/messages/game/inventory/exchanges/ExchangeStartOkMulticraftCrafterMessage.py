from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeStartOkMulticraftCrafterMessage(NetworkMessage):
    skillId:int
    

    def init(self, skillId:int):
        self.skillId = skillId
        
        super().__init__()
    
    