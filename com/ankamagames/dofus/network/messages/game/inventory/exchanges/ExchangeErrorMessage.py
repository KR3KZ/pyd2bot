from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ExchangeErrorMessage(INetworkMessage):
    protocolId = 6446
    errorType:int
    
    
