from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class DebugInClientMessage(NetworkMessage):
    level:int
    message:str
    

    def init(self, level:int, message:str):
        self.level = level
        self.message = message
        
        super().__init__()
    
    