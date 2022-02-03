from com.ankamagames.dofus.network.types.common.basic.StatisticData import StatisticData


class StatisticDataString(StatisticData):
    value:str
    

    def init(self, value:str):
        self.value = value
        
        super().__init__()
    
    