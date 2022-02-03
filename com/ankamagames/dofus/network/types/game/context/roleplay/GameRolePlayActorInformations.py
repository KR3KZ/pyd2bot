from com.ankamagames.dofus.network.types.game.context.GameContextActorInformations import GameContextActorInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
    from com.ankamagames.dofus.network.types.game.context.EntityDispositionInformations import EntityDispositionInformations
    


class GameRolePlayActorInformations(GameContextActorInformations):
    

    def init(self, look:'EntityLook', contextualId:int, disposition:'EntityDispositionInformations'):
        
        super().__init__(look, contextualId, disposition)
    
    