from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ExchangeCraftResultMessage(INetworkMessage):
    protocolId = 8524
    craftResult:int
    
    
