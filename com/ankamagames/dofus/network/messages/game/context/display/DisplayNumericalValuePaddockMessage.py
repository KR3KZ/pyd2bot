from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class DisplayNumericalValuePaddockMessage(NetworkMessage):
    rideId:int
    value:int
    type:int
    

    def init(self, rideId:int, value:int, type:int):
        self.rideId = rideId
        self.value = value
        self.type = type
        
        super().__init__()
    
    