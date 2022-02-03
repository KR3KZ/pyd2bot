from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameContextKickMessage(NetworkMessage):
    targetId:int
    

    def init(self, targetId:int):
        self.targetId = targetId
        
        super().__init__()
    
    