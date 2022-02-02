from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class PartyMemberGeoPosition(NetworkMessage):
    memberId:int
    worldX:int
    worldY:int
    mapId:int
    subAreaId:int
    
    
    def __post_init__(self):
        super().__init__()
    