from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook


class ContactLookMessage(INetworkMessage):
    protocolId = 6590
    requestId:int
    playerName:str
    playerId:int
    look:EntityLook
    
    
