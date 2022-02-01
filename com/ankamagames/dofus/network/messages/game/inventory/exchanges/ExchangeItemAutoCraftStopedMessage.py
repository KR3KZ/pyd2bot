from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ExchangeItemAutoCraftStopedMessage(INetworkMessage):
    protocolId = 470
    reason:int
    
    
