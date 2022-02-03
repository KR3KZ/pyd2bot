from com.ankamagames.dofus.network.types.game.context.roleplay.GameRolePlayNamedActorInformations import GameRolePlayNamedActorInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
    from com.ankamagames.dofus.network.types.game.context.EntityDispositionInformations import EntityDispositionInformations
    


class GameRolePlayMountInformations(GameRolePlayNamedActorInformations):
    ownerName:str
    level:int
    

    def init(self, ownerName:str, level:int, name:str, look:'EntityLook', contextualId:int, disposition:'EntityDispositionInformations'):
        self.ownerName = ownerName
        self.level = level
        
        super().__init__(name, look, contextualId, disposition)
    
    