from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook


class IndexedEntityLook(NetworkMessage):
    protocolId = 1904
    look:EntityLook
    index:int
    
