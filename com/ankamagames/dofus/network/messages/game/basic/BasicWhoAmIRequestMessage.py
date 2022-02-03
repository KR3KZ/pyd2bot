from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class BasicWhoAmIRequestMessage(NetworkMessage):
    verbose:bool
    

    def init(self, verbose:bool):
        self.verbose = verbose
        
        super().__init__()
    
    