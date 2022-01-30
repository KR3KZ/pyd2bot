from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook


class SubEntity(NetworkMessage):
    protocolId = 8670
    bindingPointCategory:int
    bindingPointIndex:int
    subEntityLook:EntityLook
    
