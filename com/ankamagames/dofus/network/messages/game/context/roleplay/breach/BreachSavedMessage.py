from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class BreachSavedMessage(NetworkMessage):
    saved:bool
    

    def init(self, saved:bool):
        self.saved = saved
        
        super().__init__()
    
    