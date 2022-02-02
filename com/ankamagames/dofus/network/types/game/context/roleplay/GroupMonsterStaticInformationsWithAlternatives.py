from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.context.roleplay.GroupMonsterStaticInformations import GroupMonsterStaticInformations
from com.ankamagames.dofus.network.types.game.context.roleplay.AlternativeMonstersInGroupLightInformations import AlternativeMonstersInGroupLightInformations


@dataclass
class GroupMonsterStaticInformationsWithAlternatives(GroupMonsterStaticInformations):
    alternatives:list[AlternativeMonstersInGroupLightInformations]
    
    
    def __post_init__(self):
        super().__init__()
    