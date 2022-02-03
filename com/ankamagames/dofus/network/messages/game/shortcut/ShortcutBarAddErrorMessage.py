from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ShortcutBarAddErrorMessage(NetworkMessage):
    error:int
    

    def init(self, error:int):
        self.error = error
        
        super().__init__()
    
    