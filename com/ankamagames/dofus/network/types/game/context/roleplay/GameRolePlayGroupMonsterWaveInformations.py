from com.ankamagames.dofus.network.types.game.context.roleplay.GameRolePlayGroupMonsterInformations import GameRolePlayGroupMonsterInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.GroupMonsterStaticInformations import GroupMonsterStaticInformations
    from com.ankamagames.dofus.network.types.game.context.roleplay.GroupMonsterStaticInformations import GroupMonsterStaticInformations
    from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
    from com.ankamagames.dofus.network.types.game.context.EntityDispositionInformations import EntityDispositionInformations
    


class GameRolePlayGroupMonsterWaveInformations(GameRolePlayGroupMonsterInformations):
    nbWaves:int
    alternatives:list['GroupMonsterStaticInformations']
    

    def init(self, nbWaves:int, alternatives:list['GroupMonsterStaticInformations'], staticInfos:'GroupMonsterStaticInformations', lootShare:int, alignmentSide:int, look:'EntityLook', contextualId:int, disposition:'EntityDispositionInformations'):
        self.nbWaves = nbWaves
        self.alternatives = alternatives
        
        super().__init__(staticInfos, lootShare, alignmentSide, look, contextualId, disposition)
    
    