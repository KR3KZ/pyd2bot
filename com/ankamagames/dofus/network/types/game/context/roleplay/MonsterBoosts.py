from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class MonsterBoosts(INetworkMessage):
    protocolId = 7719
    id:int
    xpBoost:int
    dropBoost:int
    
    
