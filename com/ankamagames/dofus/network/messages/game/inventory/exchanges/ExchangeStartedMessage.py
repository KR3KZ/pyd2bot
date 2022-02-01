from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ExchangeStartedMessage(INetworkMessage):
    protocolId = 8540
    exchangeType:int
    
    
