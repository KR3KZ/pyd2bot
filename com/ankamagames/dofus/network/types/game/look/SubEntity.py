from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook


class SubEntity(INetworkMessage):
    protocolId = 8670
    bindingPointCategory:int
    bindingPointIndex:int
    subEntityLook:'EntityLook'
    
    
