from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class CheckIntegrityMessage(NetworkMessage):
    data:list[int]
    

    def init(self, data:list[int]):
        self.data = data
        
        super().__init__()
    
    