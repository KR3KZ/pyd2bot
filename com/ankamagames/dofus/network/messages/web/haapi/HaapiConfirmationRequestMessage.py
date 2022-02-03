from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class HaapiConfirmationRequestMessage(NetworkMessage):
    kamas:int
    ogrines:int
    rate:int
    action:int
    

    def init(self, kamas:int, ogrines:int, rate:int, action:int):
        self.kamas = kamas
        self.ogrines = ogrines
        self.rate = rate
        self.action = action
        
        super().__init__()
    
    