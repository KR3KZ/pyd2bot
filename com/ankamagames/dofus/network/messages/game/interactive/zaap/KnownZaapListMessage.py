from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class KnownZaapListMessage(NetworkMessage):
    destinations:list[int]
    

    def init(self, destinations:list[int]):
        self.destinations = destinations
        
        super().__init__()
    
    