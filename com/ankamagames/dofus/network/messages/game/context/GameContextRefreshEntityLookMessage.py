from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
    


class GameContextRefreshEntityLookMessage(NetworkMessage):
    id:int
    look:'EntityLook'
    

    def init(self, id:int, look:'EntityLook'):
        self.id = id
        self.look = look
        
        super().__init__()
    
    