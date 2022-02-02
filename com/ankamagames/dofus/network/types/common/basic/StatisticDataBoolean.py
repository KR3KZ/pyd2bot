from dataclasses import dataclass
from com.ankamagames.dofus.network.types.common.basic.StatisticData import StatisticData


@dataclass
class StatisticDataBoolean(StatisticData):
    value:bool
    
    
    def __post_init__(self):
        super().__init__()
    