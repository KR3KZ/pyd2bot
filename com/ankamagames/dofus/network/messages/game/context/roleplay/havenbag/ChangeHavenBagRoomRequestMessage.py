from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ChangeHavenBagRoomRequestMessage(NetworkMessage):
    roomId:int
    

    def init(self, roomId:int):
        self.roomId = roomId
        
        super().__init__()
    
    