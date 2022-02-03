from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ObjectAveragePricesMessage(NetworkMessage):
    ids:list[int]
    avgPrices:list[int]
    

    def init(self, ids:list[int], avgPrices:list[int]):
        self.ids = ids
        self.avgPrices = avgPrices
        
        super().__init__()
    
    