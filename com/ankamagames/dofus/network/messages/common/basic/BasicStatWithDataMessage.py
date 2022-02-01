from com.ankamagames.dofus.network.messages.common.basic.BasicStatMessage import BasicStatMessage
from com.ankamagames.dofus.network.types.common.basic.StatisticData import StatisticData


class BasicStatWithDataMessage(BasicStatMessage):
    datas:list[StatisticData]
    
    
