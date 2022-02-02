from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.context.roleplay.MonsterInGroupLightInformations import MonsterInGroupLightInformations
from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook


@dataclass
class MonsterInGroupInformations(MonsterInGroupLightInformations):
    look:EntityLook
    
    
    def __post_init__(self):
        super().__init__()
    