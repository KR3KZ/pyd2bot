from com.ankamagames.dofus.network.types.game.context.roleplay.GameRolePlayActorInformations import GameRolePlayActorInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.GroupMonsterStaticInformations import GroupMonsterStaticInformations
    from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
    from com.ankamagames.dofus.network.types.game.context.EntityDispositionInformations import EntityDispositionInformations
    


class GameRolePlayGroupMonsterInformations(GameRolePlayActorInformations):
    staticInfos:'GroupMonsterStaticInformations'
    lootShare:int
    alignmentSide:int
    keyRingBonus:bool
    hasHardcoreDrop:bool
    hasAVARewardToken:bool
    

    def init(self, staticInfos:'GroupMonsterStaticInformations', lootShare:int, alignmentSide:int, look:'EntityLook', contextualId:int, disposition:'EntityDispositionInformations'):
        self.staticInfos = staticInfos
        self.lootShare = lootShare
        self.alignmentSide = alignmentSide
        
        super().__init__(look, contextualId, disposition)
    
    