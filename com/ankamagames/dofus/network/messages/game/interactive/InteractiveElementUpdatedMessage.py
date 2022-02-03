from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.interactive.InteractiveElement import InteractiveElement
    


class InteractiveElementUpdatedMessage(NetworkMessage):
    interactiveElement:'InteractiveElement'
    

    def init(self, interactiveElement:'InteractiveElement'):
        self.interactiveElement = interactiveElement
        
        super().__init__()
    
    