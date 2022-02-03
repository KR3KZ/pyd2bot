from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class MountFeedRequestMessage(NetworkMessage):
    mountUid:int
    mountLocation:int
    mountFoodUid:int
    quantity:int
    

    def init(self, mountUid:int, mountLocation:int, mountFoodUid:int, quantity:int):
        self.mountUid = mountUid
        self.mountLocation = mountLocation
        self.mountFoodUid = mountFoodUid
        self.quantity = quantity
        
        super().__init__()
    
    