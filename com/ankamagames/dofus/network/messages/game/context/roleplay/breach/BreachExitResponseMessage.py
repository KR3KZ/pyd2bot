from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class BreachExitResponseMessage(NetworkMessage):
    exited:bool
    

    def init(self, exited:bool):
        self.exited = exited
        
        super().__init__()
    
    