from com.ankamagames.dofus.network.types.game.paddock.PaddockInformations import PaddockInformations
from com.ankamagames.dofus.network.types.game.paddock.MountInformationsForPaddock import MountInformationsForPaddock


class PaddockContentInformations(PaddockInformations):
    protocolId = 8051
    paddockId:float
    worldX:int
    worldY:int
    mapId:float
    subAreaId:int
    abandonned:bool
    mountsInformations:list[MountInformationsForPaddock]
    
