from com.ankamagames.dofus.network.types.game.context.roleplay.GameRolePlayActorInformations import GameRolePlayActorInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.prism.PrismInformation import PrismInformation
    from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
    from com.ankamagames.dofus.network.types.game.context.EntityDispositionInformations import EntityDispositionInformations
    


class GameRolePlayPrismInformations(GameRolePlayActorInformations):
    prism:'PrismInformation'
    

    def init(self, prism:'PrismInformation', look:'EntityLook', contextualId:int, disposition:'EntityDispositionInformations'):
        self.prism = prism
        
        super().__init__(look, contextualId, disposition)
    
    