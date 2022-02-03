from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ProtocolRequired(NetworkMessage):
    version:str
    

    def init(self, version:str):
        self.version = version
        
        super().__init__()
    
    