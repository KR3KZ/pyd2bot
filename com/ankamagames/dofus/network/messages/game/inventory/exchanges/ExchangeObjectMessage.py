from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ExchangeObjectMessage(INetworkMessage):
    protocolId = 1966
    remote:bool
    
    
