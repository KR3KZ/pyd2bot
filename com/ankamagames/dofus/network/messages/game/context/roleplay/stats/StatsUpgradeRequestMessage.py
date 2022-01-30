from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class StatsUpgradeRequestMessage(INetworkMessage):
    protocolId = 327
    useAdditionnal:bool
    statId:int
    boostPoint:int
    
    
