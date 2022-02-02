from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.common.basic.BasicStatMessage import BasicStatMessage
from com.ankamagames.dofus.network.types.common.basic.StatisticData import StatisticData


@dataclass
class BasicStatWithDataMessage(BasicStatMessage):
    datas:list[StatisticData]
    
    
    def __post_init__(self):
        super().__init__()
    