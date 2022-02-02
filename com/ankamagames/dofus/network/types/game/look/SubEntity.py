from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook


@dataclass
class SubEntity(NetworkMessage):
    bindingPointCategory:int
    bindingPointIndex:int
    subEntityLook:'EntityLook'
    
    
    def __post_init__(self):
        super().__init__()
    