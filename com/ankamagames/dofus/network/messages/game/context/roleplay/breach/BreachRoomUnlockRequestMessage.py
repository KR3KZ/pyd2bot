from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class BreachRoomUnlockRequestMessage(NetworkMessage):
    roomId:int
    

    def init(self, roomId:int):
        self.roomId = roomId
        
        super().__init__()
    
    