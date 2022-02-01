from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class PrismFightSwapRequestMessage(INetworkMessage):
    protocolId = 4070
    subAreaId:int
    targetId:int
    
    
