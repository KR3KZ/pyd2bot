from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.data.items.ObjectItem import ObjectItem
    


class ObjectsAddedMessage(NetworkMessage):
    object:list['ObjectItem']
    

    def init(self, object:list['ObjectItem']):
        self.object = object
        
        super().__init__()
    
    