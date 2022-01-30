from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook


class IndexedEntityLook(INetworkMessage):
    protocolId = 1904
    look:EntityLook
    index:int
    
    
