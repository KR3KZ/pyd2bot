from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class BasicPingMessage(NetworkMessage):
    quiet:bool
    

    def init(self, quiet:bool):
        self.quiet = quiet
        
        super().__init__()
    
    