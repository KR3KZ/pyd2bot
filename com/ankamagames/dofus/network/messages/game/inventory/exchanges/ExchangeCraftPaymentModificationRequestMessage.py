from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ExchangeCraftPaymentModificationRequestMessage(INetworkMessage):
    protocolId = 5785
    quantity:int
    
    
