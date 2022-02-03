from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.interactive.InteractiveElement import InteractiveElement
    


class InteractiveMapUpdateMessage(NetworkMessage):
    interactiveElements:list['InteractiveElement']
    

    def init(self, interactiveElements:list['InteractiveElement']):
        self.interactiveElements = interactiveElements
        
        super().__init__()
    
    