from com.ankamagames.dofus.network.types.game.context.roleplay.GameRolePlayActorInformations import GameRolePlayActorInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
    from com.ankamagames.dofus.network.types.game.context.EntityDispositionInformations import EntityDispositionInformations
    


class GameRolePlayNpcInformations(GameRolePlayActorInformations):
    npcId:int
    sex:bool
    specialArtworkId:int
    

    def init(self, npcId:int, sex:bool, specialArtworkId:int, look:'EntityLook', contextualId:int, disposition:'EntityDispositionInformations'):
        self.npcId = npcId
        self.sex = sex
        self.specialArtworkId = specialArtworkId
        
        super().__init__(look, contextualId, disposition)
    
    