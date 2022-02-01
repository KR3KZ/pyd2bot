from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class MonsterBoosts(INetworkMessage):
    protocolId = 7719
    id:int
    xpBoost:int
    dropBoost:int
    
    
