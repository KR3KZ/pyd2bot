from com.ankamagames.dofus.network.types.game.context.roleplay.GameRolePlayActorInformations import GameRolePlayActorInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
    from com.ankamagames.dofus.network.types.game.context.EntityDispositionInformations import EntityDispositionInformations
    


class GameRolePlayTreasureHintInformations(GameRolePlayActorInformations):
    npcId:int
    

    def init(self, npcId:int, look:'EntityLook', contextualId:int, disposition:'EntityDispositionInformations'):
        self.npcId = npcId
        
        super().__init__(look, contextualId, disposition)
    
    