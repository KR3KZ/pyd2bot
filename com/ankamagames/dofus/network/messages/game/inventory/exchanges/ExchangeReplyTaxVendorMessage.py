from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ExchangeReplyTaxVendorMessage(INetworkMessage):
    protocolId = 7870
    objectValue:int
    totalTaxValue:int
    
    
