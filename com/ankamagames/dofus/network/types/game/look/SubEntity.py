from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook


class SubEntity(INetworkMessage):
    protocolId = 8670
    bindingPointCategory:int
    bindingPointIndex:int
    subEntityLook:EntityLook
    
    
