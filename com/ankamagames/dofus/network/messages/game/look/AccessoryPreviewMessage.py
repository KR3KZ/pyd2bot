from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
    


class AccessoryPreviewMessage(NetworkMessage):
    look:'EntityLook'
    

    def init(self, look:'EntityLook'):
        self.look = look
        
        super().__init__()
    
    