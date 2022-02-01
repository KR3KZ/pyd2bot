from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class PrismInfoInValidMessage(INetworkMessage):
    protocolId = 7307
    reason:int
    
    
