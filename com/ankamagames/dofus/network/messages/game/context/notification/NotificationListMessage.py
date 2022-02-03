from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class NotificationListMessage(NetworkMessage):
    flags:list[int]
    

    def init(self, flags:list[int]):
        self.flags = flags
        
        super().__init__()
    
    