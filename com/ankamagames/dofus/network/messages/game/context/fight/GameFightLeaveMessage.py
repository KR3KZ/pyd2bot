from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameFightLeaveMessage(NetworkMessage):
    charId:int
    

    def init(self, charId:int):
        self.charId = charId
        
        super().__init__()
    
    