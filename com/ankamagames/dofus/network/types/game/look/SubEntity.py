from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
    


class SubEntity(NetworkMessage):
    bindingPointCategory:int
    bindingPointIndex:int
    subEntityLook:'EntityLook'
    

    def init(self, bindingPointCategory:int, bindingPointIndex:int, subEntityLook:'EntityLook'):
        self.bindingPointCategory = bindingPointCategory
        self.bindingPointIndex = bindingPointIndex
        self.subEntityLook = subEntityLook
        
        super().__init__()
    
    