from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class LivingObjectDissociateMessage(NetworkMessage):
    livingUID:int
    livingPosition:int
    

    def init(self, livingUID:int, livingPosition:int):
        self.livingUID = livingUID
        self.livingPosition = livingPosition
        
        super().__init__()
    
    