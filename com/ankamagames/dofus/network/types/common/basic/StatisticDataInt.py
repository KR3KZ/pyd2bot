from com.ankamagames.dofus.network.types.common.basic.StatisticData import StatisticData


class StatisticDataInt(StatisticData):
    value:int
    

    def init(self, value:int):
        self.value = value
        
        super().__init__()
    
    