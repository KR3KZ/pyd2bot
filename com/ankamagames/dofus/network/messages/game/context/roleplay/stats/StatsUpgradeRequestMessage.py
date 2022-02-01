from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class StatsUpgradeRequestMessage(NetworkMessage):
    useAdditionnal:bool
    statId:int
    boostPoint:int
    
    
