from com.ankamagames.dofus.network.types.game.paddock.PaddockInformations import PaddockInformations
from com.ankamagames.dofus.network.types.game.paddock.MountInformationsForPaddock import MountInformationsForPaddock


class PaddockContentInformations(PaddockInformations):
    paddockId:int
    worldX:int
    worldY:int
    mapId:int
    subAreaId:int
    abandonned:bool
    mountsInformations:list[MountInformationsForPaddock]
    
    
