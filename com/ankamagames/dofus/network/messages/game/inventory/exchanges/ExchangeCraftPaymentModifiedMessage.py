from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ExchangeCraftPaymentModifiedMessage(INetworkMessage):
    protocolId = 8641
    goldSum:int
    
    
