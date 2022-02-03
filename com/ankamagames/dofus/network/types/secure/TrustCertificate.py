from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class TrustCertificate(NetworkMessage):
    id:int
    hash:str
    

    def init(self, id:int, hash:str):
        self.id = id
        self.hash = hash
        
        super().__init__()
    
    