from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class LivingObjectChangeSkinRequestMessage(NetworkMessage):
    livingUID:int
    livingPosition:int
    skinId:int
    

    def init(self, livingUID:int, livingPosition:int, skinId:int):
        self.livingUID = livingUID
        self.livingPosition = livingPosition
        self.skinId = skinId
        
        super().__init__()
    
    