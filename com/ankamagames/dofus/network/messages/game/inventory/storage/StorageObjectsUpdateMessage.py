from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.data.items.ObjectItem import ObjectItem
    


class StorageObjectsUpdateMessage(NetworkMessage):
    objectList:list['ObjectItem']
    

    def init(self, objectList:list['ObjectItem']):
        self.objectList = objectList
        
        super().__init__()
    
    