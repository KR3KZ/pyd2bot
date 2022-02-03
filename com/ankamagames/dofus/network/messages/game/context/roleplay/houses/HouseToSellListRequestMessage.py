from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class HouseToSellListRequestMessage(NetworkMessage):
    pageIndex:int
    

    def init(self, pageIndex:int):
        self.pageIndex = pageIndex
        
        super().__init__()
    
    