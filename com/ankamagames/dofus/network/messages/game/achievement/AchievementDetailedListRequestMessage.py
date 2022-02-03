from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class AchievementDetailedListRequestMessage(NetworkMessage):
    categoryId:int
    

    def init(self, categoryId:int):
        self.categoryId = categoryId
        
        super().__init__()
    
    