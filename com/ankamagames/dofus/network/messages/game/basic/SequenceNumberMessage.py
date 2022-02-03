from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class SequenceNumberMessage(NetworkMessage):
    number:int
    

    def init(self, number:int):
        self.number = number
        
        super().__init__()
    
    