from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ExchangeWaitingResultMessage(INetworkMessage):
    protocolId = 4369
    bwait:bool
    
    
