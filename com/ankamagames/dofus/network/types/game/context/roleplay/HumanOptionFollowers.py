from com.ankamagames.dofus.network.types.game.context.roleplay.HumanOption import HumanOption
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.look.IndexedEntityLook import IndexedEntityLook
    


class HumanOptionFollowers(HumanOption):
    followingCharactersLook:list['IndexedEntityLook']
    

    def init(self, followingCharactersLook:list['IndexedEntityLook']):
        self.followingCharactersLook = followingCharactersLook
        
        super().__init__()
    
    