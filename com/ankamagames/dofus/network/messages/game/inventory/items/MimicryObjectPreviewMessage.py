from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.data.items.ObjectItem import ObjectItem
    


class MimicryObjectPreviewMessage(NetworkMessage):
    result:'ObjectItem'
    

    def init(self, result:'ObjectItem'):
        self.result = result
        
        super().__init__()
    
    