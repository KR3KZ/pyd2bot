from com.ankamagames.dofus.network.messages.common.basic.BasicStatMessage import BasicStatMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.common.basic.StatisticData import StatisticData
    


class BasicStatWithDataMessage(BasicStatMessage):
    datas:list['StatisticData']
    

    def init(self, datas:list['StatisticData'], timeSpent:int, statId:int):
        self.datas = datas
        
        super().__init__(timeSpent, statId)
    
    