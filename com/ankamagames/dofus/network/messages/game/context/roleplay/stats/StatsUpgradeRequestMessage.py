from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class StatsUpgradeRequestMessage(NetworkMessage):
    protocolId = 327
    useAdditionnal:bool
    statId:int
    boostPoint:int
    
    
