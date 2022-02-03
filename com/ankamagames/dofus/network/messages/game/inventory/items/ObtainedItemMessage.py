from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ObtainedItemMessage(NetworkMessage):
    genericId:int
    baseQuantity:int
    

    def init(self, genericId:int, baseQuantity:int):
        self.genericId = genericId
        self.baseQuantity = baseQuantity
        
        super().__init__()
    
    