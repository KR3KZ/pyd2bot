from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class AccountLoggingKickedMessage(NetworkMessage):
    days:int
    hours:int
    minutes:int
    

    def init(self, days:int, hours:int, minutes:int):
        self.days = days
        self.hours = hours
        self.minutes = minutes
        
        super().__init__()
    
    