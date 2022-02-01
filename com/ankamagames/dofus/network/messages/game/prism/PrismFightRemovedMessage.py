from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class PrismFightRemovedMessage(INetworkMessage):
    protocolId = 9563
    subAreaId:int
    
    
