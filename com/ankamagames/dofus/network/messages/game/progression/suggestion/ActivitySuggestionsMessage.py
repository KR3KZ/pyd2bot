from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ActivitySuggestionsMessage(NetworkMessage):
    lockedActivitiesIds:list[int]
    unlockedActivitiesIds:list[int]
    

    def init(self, lockedActivitiesIds:list[int], unlockedActivitiesIds:list[int]):
        self.lockedActivitiesIds = lockedActivitiesIds
        self.unlockedActivitiesIds = unlockedActivitiesIds
        
        super().__init__()
    
    