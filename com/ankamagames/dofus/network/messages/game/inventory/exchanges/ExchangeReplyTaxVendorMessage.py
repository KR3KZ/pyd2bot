from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeReplyTaxVendorMessage(NetworkMessage):
    objectValue:int
    totalTaxValue:int
    

    def init(self, objectValue:int, totalTaxValue:int):
        self.objectValue = objectValue
        self.totalTaxValue = totalTaxValue
        
        super().__init__()
    
    