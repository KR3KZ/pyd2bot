from com.ankamagames.dofus.network.types.game.context.roleplay.GameRolePlayActorInformations import GameRolePlayActorInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
    from com.ankamagames.dofus.network.types.game.context.EntityDispositionInformations import EntityDispositionInformations
    


class GameRolePlayNamedActorInformations(GameRolePlayActorInformations):
    name:str
    

    def init(self, name:str, look:'EntityLook', contextualId:int, disposition:'EntityDispositionInformations'):
        self.name = name
        
        super().__init__(look, contextualId, disposition)
    
    