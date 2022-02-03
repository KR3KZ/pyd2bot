from com.ankamagames.dofus.network.types.game.paddock.PaddockInformations import PaddockInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.paddock.MountInformationsForPaddock import MountInformationsForPaddock
    


class PaddockContentInformations(PaddockInformations):
    paddockId:int
    worldX:int
    worldY:int
    mapId:int
    subAreaId:int
    abandonned:bool
    mountsInformations:list['MountInformationsForPaddock']
    

    def init(self, paddockId:int, worldX:int, worldY:int, mapId:int, subAreaId:int, abandonned:bool, mountsInformations:list['MountInformationsForPaddock'], maxOutdoorMount:int, maxItems:int):
        self.paddockId = paddockId
        self.worldX = worldX
        self.worldY = worldY
        self.mapId = mapId
        self.subAreaId = subAreaId
        self.abandonned = abandonned
        self.mountsInformations = mountsInformations
        
        super().__init__(maxOutdoorMount, maxItems)
    
    