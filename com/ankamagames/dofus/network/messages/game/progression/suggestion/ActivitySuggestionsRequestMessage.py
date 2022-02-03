from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ActivitySuggestionsRequestMessage(NetworkMessage):
    minLevel:int
    maxLevel:int
    areaId:int
    activityCategoryId:int
    nbCards:int
    

    def init(self, minLevel:int, maxLevel:int, areaId:int, activityCategoryId:int, nbCards:int):
        self.minLevel = minLevel
        self.maxLevel = maxLevel
        self.areaId = areaId
        self.activityCategoryId = activityCategoryId
        self.nbCards = nbCards
        
        super().__init__()
    
    