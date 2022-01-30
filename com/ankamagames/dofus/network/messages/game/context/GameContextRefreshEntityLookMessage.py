from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook


class GameContextRefreshEntityLookMessage(NetworkMessage):
    protocolId = 5261
    id:int
    look:EntityLook
    
    
