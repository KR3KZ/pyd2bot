from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class StatsUpgradeRequestMessage(INetworkMessage):
    protocolId = 327
    useAdditionnal:bool
    statId:int
    boostPoint:int
    
    
