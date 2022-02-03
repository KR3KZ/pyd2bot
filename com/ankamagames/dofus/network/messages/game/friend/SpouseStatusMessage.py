from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class SpouseStatusMessage(NetworkMessage):
    hasSpouse:bool
    

    def init(self, hasSpouse:bool):
        self.hasSpouse = hasSpouse
        
        super().__init__()
    
    