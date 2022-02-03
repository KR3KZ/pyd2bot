from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class AdditionalTaxCollectorInformations(NetworkMessage):
    collectorCallerName:str
    date:int
    

    def init(self, collectorCallerName:str, date:int):
        self.collectorCallerName = collectorCallerName
        self.date = date
        
        super().__init__()
    
    