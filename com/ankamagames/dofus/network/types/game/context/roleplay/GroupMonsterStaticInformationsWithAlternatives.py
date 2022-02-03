from com.ankamagames.dofus.network.types.game.context.roleplay.GroupMonsterStaticInformations import GroupMonsterStaticInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.AlternativeMonstersInGroupLightInformations import AlternativeMonstersInGroupLightInformations
    from com.ankamagames.dofus.network.types.game.context.roleplay.MonsterInGroupLightInformations import MonsterInGroupLightInformations
    from com.ankamagames.dofus.network.types.game.context.roleplay.MonsterInGroupInformations import MonsterInGroupInformations
    


class GroupMonsterStaticInformationsWithAlternatives(GroupMonsterStaticInformations):
    alternatives:list['AlternativeMonstersInGroupLightInformations']
    

    def init(self, alternatives:list['AlternativeMonstersInGroupLightInformations'], mainCreatureLightInfos:'MonsterInGroupLightInformations', underlings:list['MonsterInGroupInformations']):
        self.alternatives = alternatives
        
        super().__init__(mainCreatureLightInfos, underlings)
    
    