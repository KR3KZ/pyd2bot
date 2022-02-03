from com.ankamagames.dofus.network.types.common.basic.StatisticData import StatisticData


class StatisticDataByte(StatisticData):
    value:int
    

    def init(self, value:int):
        self.value = value
        
        super().__init__()
    
    