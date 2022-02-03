from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class BufferInformation(NetworkMessage):
    id:int
    amount:int
    

    def init(self, id:int, amount:int):
        self.id = id
        self.amount = amount
        
        super().__init__()
    
    