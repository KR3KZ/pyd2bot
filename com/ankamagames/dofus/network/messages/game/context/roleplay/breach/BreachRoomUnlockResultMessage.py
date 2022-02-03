from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class BreachRoomUnlockResultMessage(NetworkMessage):
    roomId:int
    result:int
    

    def init(self, roomId:int, result:int):
        self.roomId = roomId
        self.result = result
        
        super().__init__()
    
    