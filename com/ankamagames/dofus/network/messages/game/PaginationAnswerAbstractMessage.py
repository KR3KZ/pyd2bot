from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class PaginationAnswerAbstractMessage(NetworkMessage):
    offset:int
    count:int
    total:int
    

    def init(self, offset:int, count:int, total:int):
        self.offset = offset
        self.count = count
        self.total = total
        
        super().__init__()
    
    