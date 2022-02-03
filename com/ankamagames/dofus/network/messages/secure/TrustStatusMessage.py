from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class TrustStatusMessage(NetworkMessage):
    trusted:bool
    certified:bool
    

    def init(self):
        
        super().__init__()
    
    