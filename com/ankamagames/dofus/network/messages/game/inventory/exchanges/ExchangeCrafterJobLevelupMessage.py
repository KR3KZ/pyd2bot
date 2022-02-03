from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeCrafterJobLevelupMessage(NetworkMessage):
    crafterJobLevel:int
    

    def init(self, crafterJobLevel:int):
        self.crafterJobLevel = crafterJobLevel
        
        super().__init__()
    
    