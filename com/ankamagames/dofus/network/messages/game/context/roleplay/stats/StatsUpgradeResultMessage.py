from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class StatsUpgradeResultMessage(INetworkMessage):
    protocolId = 4083
    result:int
    nbCharacBoost:int
    
    
