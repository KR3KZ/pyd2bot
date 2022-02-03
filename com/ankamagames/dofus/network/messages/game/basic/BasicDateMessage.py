from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class BasicDateMessage(NetworkMessage):
    day:int
    month:int
    year:int
    

    def init(self, day:int, month:int, year:int):
        self.day = day
        self.month = month
        self.year = year
        
        super().__init__()
    
    