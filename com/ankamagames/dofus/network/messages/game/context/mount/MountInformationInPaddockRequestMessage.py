from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class MountInformationInPaddockRequestMessage(NetworkMessage):
    mapRideId:int
    

    def init(self, mapRideId:int):
        self.mapRideId = mapRideId
        
        super().__init__()
    
    