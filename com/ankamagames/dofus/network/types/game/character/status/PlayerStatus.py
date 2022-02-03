from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class PlayerStatus(NetworkMessage):
    statusId:int
    

    def init(self, statusId:int):
        self.statusId = statusId
        
        super().__init__()
    
    