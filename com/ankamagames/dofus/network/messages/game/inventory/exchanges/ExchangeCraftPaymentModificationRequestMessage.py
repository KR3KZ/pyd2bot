from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ExchangeCraftPaymentModificationRequestMessage(INetworkMessage):
    protocolId = 5785
    quantity:int
    
    
