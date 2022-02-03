from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class NotificationUpdateFlagMessage(NetworkMessage):
    index:int
    

    def init(self, index:int):
        self.index = index
        
        super().__init__()
    
    