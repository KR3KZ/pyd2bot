from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class AlmanachCalendarDateMessage(NetworkMessage):
    date:int
    

    def init(self, date:int):
        self.date = date
        
        super().__init__()
    
    