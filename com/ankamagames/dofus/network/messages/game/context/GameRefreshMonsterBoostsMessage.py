from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.MonsterBoosts import MonsterBoosts
from com.ankamagames.dofus.network.types.game.context.roleplay.MonsterBoosts import MonsterBoosts


class GameRefreshMonsterBoostsMessage(NetworkMessage):
    monsterBoosts:list[MonsterBoosts]
    familyBoosts:list[MonsterBoosts]
    
    
