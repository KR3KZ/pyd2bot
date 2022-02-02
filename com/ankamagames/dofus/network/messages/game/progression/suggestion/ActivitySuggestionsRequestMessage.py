from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class ActivitySuggestionsRequestMessage(NetworkMessage):
    minLevel:int
    maxLevel:int
    areaId:int
    activityCategoryId:int
    nbCards:int
    
    
    def __post_init__(self):
        super().__init__()
    