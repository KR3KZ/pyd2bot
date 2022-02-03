from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeOnHumanVendorRequestMessage(NetworkMessage):
    humanVendorId:int
    humanVendorCell:int
    

    def init(self, humanVendorId:int, humanVendorCell:int):
        self.humanVendorId = humanVendorId
        self.humanVendorCell = humanVendorCell
        
        super().__init__()
    
    