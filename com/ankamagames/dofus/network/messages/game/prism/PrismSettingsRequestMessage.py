from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class PrismSettingsRequestMessage(NetworkMessage):
    subAreaId:int
    startDefenseTime:int
    
    
    def __post_init__(self):
        super().__init__()
    