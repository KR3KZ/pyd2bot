from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.data.items.ObjectItem import ObjectItem
    


class ExchangeStartedTaxCollectorShopMessage(NetworkMessage):
    objects:list['ObjectItem']
    kamas:int
    

    def init(self, objects:list['ObjectItem'], kamas:int):
        self.objects = objects
        self.kamas = kamas
        
        super().__init__()
    
    