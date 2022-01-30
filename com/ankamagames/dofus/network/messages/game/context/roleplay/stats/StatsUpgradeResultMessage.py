from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class StatsUpgradeResultMessage(INetworkMessage):
    protocolId = 4083
    result:int
    nbCharacBoost:int
    
    
