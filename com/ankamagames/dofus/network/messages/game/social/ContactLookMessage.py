from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
    


class ContactLookMessage(NetworkMessage):
    requestId:int
    playerName:str
    playerId:int
    look:'EntityLook'
    

    def init(self, requestId:int, playerName:str, playerId:int, look:'EntityLook'):
        self.requestId = requestId
        self.playerName = playerName
        self.playerId = playerId
        self.look = look
        
        super().__init__()
    
    