from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook


class ContactLookMessage(NetworkMessage):
    protocolId = 6590
    requestId:int
    playerName:str
    playerId:int
    look:EntityLook
    
    
