from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class PaginationRequestAbstractMessage(NetworkMessage):
    offset:int
    count:int
    

    def init(self, offset:int, count:int):
        self.offset = offset
        self.count = count
        
        super().__init__()
    
    