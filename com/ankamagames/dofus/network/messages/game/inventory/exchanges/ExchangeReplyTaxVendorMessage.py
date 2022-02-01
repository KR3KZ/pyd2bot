from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ExchangeReplyTaxVendorMessage(INetworkMessage):
    protocolId = 7870
    objectValue:int
    totalTaxValue:int
    
    
