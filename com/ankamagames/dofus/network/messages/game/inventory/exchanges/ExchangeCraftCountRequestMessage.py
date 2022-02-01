from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ExchangeCraftCountRequestMessage(INetworkMessage):
    protocolId = 7316
    count:int
    
    
