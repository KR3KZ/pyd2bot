from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.MonsterBoosts import MonsterBoosts
from com.ankamagames.dofus.network.types.game.context.roleplay.MonsterBoosts import MonsterBoosts


class GameRefreshMonsterBoostsMessage(NetworkMessage):
    protocolId = 2110
    monsterBoosts:list[MonsterBoosts]
    familyBoosts:list[MonsterBoosts]
    
