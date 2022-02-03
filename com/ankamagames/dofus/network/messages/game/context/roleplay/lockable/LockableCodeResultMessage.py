from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class LockableCodeResultMessage(NetworkMessage):
    result:int
    

    def init(self, result:int):
        self.result = result
        
        super().__init__()
    
    