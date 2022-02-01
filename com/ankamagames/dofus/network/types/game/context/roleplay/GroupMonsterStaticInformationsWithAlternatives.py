from com.ankamagames.dofus.network.types.game.context.roleplay.GroupMonsterStaticInformations import GroupMonsterStaticInformations
from com.ankamagames.dofus.network.types.game.context.roleplay.AlternativeMonstersInGroupLightInformations import AlternativeMonstersInGroupLightInformations


class GroupMonsterStaticInformationsWithAlternatives(GroupMonsterStaticInformations):
    alternatives:list[AlternativeMonstersInGroupLightInformations]
    
    
