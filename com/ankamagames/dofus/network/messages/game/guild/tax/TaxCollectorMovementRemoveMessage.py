from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class TaxCollectorMovementRemoveMessage(NetworkMessage):
    collectorId:int
    

    def init(self, collectorId:int):
        self.collectorId = collectorId
        
        super().__init__()
    
    