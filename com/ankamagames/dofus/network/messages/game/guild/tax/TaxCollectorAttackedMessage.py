from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.BasicGuildInformations import BasicGuildInformations


@dataclass
class TaxCollectorAttackedMessage(NetworkMessage):
    firstNameId:int
    lastNameId:int
    worldX:int
    worldY:int
    mapId:int
    subAreaId:int
    guild:BasicGuildInformations
    
    
    def __post_init__(self):
        super().__init__()
    