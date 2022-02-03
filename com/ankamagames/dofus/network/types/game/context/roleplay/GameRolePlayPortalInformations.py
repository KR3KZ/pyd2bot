from com.ankamagames.dofus.network.types.game.context.roleplay.GameRolePlayActorInformations import GameRolePlayActorInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.treasureHunt.PortalInformation import PortalInformation
    from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
    from com.ankamagames.dofus.network.types.game.context.EntityDispositionInformations import EntityDispositionInformations
    


class GameRolePlayPortalInformations(GameRolePlayActorInformations):
    portal:'PortalInformation'
    

    def init(self, portal:'PortalInformation', look:'EntityLook', contextualId:int, disposition:'EntityDispositionInformations'):
        self.portal = portal
        
        super().__init__(look, contextualId, disposition)
    
    