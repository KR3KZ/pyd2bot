from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ExchangeRequestedMessage(INetworkMessage):
    protocolId = 5525
    exchangeType:int
    
    
