from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ExchangeReplyTaxVendorMessage(NetworkMessage):
    protocolId = 7870
    objectValue:int
    totalTaxValue:int
    
    
