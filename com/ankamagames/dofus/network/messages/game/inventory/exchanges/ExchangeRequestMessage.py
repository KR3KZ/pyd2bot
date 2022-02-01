from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ExchangeRequestMessage(INetworkMessage):
    protocolId = 289
    exchangeType:int
    
    
