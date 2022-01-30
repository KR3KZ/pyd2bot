from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook


class GameContextRefreshEntityLookMessage(INetworkMessage):
    protocolId = 5261
    id:int
    look:EntityLook
    
    
