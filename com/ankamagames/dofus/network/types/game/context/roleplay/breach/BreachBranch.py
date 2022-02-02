from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.MonsterInGroupLightInformations import MonsterInGroupLightInformations
from com.ankamagames.dofus.network.types.game.context.roleplay.MonsterInGroupLightInformations import MonsterInGroupLightInformations


@dataclass
class BreachBranch(NetworkMessage):
    room:int
    element:int
    bosses:list[MonsterInGroupLightInformations]
    map:int
    score:int
    relativeScore:int
    monsters:list[MonsterInGroupLightInformations]
    
    
    def __post_init__(self):
        super().__init__()
    