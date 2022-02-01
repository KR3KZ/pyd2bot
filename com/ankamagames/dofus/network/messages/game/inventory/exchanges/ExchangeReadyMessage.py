from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ExchangeReadyMessage(INetworkMessage):
    protocolId = 5849
    ready:bool
    step:int
    
    
