from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameContextCreateMessage(NetworkMessage):
    context:int
    

    def init(self, context:int):
        self.context = context
        
        super().__init__()
    
    