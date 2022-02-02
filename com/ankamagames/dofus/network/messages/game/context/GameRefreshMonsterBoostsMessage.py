from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.MonsterBoosts import MonsterBoosts
from com.ankamagames.dofus.network.types.game.context.roleplay.MonsterBoosts import MonsterBoosts


@dataclass
class GameRefreshMonsterBoostsMessage(NetworkMessage):
    monsterBoosts:list[MonsterBoosts]
    familyBoosts:list[MonsterBoosts]
    
    
    def __post_init__(self):
        super().__init__()
    