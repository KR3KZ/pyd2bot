from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook


class SubEntity(NetworkMessage):
    bindingPointCategory:int
    bindingPointIndex:int
    subEntityLook:EntityLook
    
    
