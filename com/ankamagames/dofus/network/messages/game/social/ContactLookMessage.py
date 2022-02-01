from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook


class ContactLookMessage(NetworkMessage):
    requestId:int
    playerName:str
    playerId:int
    look:EntityLook
    
    
