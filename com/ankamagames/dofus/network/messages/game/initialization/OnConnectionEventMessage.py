from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class OnConnectionEventMessage(NetworkMessage):
    eventType:int
    

    def init(self, eventType:int):
        self.eventType = eventType
        
        super().__init__()
    
    