from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class AnomalySubareaInformation(NetworkMessage):
    subAreaId:int
    rewardRate:int
    hasAnomaly:bool
    anomalyClosingTime:int
    
    
    def __post_init__(self):
        super().__init__()
    