from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ServerSessionConstant(NetworkMessage):
    id:int
    

    def init(self, id:int):
        self.id = id
        
        super().__init__()
    
    