from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class MonsterBoosts(NetworkMessage):
    protocolId = 7719
    id:int
    xpBoost:int
    dropBoost:int
    
