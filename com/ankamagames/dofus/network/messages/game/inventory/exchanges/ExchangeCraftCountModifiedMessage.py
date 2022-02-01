from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ExchangeCraftCountModifiedMessage(INetworkMessage):
    protocolId = 2567
    count:int
    
    
