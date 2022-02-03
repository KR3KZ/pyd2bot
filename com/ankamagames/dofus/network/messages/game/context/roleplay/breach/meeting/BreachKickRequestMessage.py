from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class BreachKickRequestMessage(NetworkMessage):
    target:int
    

    def init(self, target:int):
        self.target = target
        
        super().__init__()
    
    