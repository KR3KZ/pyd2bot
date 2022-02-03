from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class PrismFightRemovedMessage(NetworkMessage):
    subAreaId:int
    

    def init(self, subAreaId:int):
        self.subAreaId = subAreaId
        
        super().__init__()
    
    