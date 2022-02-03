from com.ankamagames.dofus.network.types.common.basic.StatisticData import StatisticData


class StatisticDataBoolean(StatisticData):
    value:bool
    

    def init(self, value:bool):
        self.value = value
        
        super().__init__()
    
    