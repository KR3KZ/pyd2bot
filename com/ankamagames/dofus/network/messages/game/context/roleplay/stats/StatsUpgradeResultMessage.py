from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class StatsUpgradeResultMessage(NetworkMessage):
    protocolId = 4083
    result:int
    nbCharacBoost:int
    
    
