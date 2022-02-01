from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ExchangeIsReadyMessage(INetworkMessage):
    protocolId = 6263
    id:int
    ready:bool
    
    
