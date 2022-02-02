from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.MonsterInGroupLightInformations import MonsterInGroupLightInformations


@dataclass
class AlternativeMonstersInGroupLightInformations(NetworkMessage):
    playerCount:int
    monsters:list[MonsterInGroupLightInformations]
    
    
    def __post_init__(self):
        super().__init__()
    