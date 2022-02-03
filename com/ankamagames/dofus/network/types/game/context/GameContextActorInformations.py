from com.ankamagames.dofus.network.types.game.context.GameContextActorPositionInformations import GameContextActorPositionInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
    from com.ankamagames.dofus.network.types.game.context.EntityDispositionInformations import EntityDispositionInformations
    


class GameContextActorInformations(GameContextActorPositionInformations):
    look:'EntityLook'
    

    def init(self, look:'EntityLook', contextualId:int, disposition:'EntityDispositionInformations'):
        self.look = look
        
        super().__init__(contextualId, disposition)
    
    