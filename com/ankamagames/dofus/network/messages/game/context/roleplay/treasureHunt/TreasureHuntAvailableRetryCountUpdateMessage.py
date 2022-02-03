from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class TreasureHuntAvailableRetryCountUpdateMessage(NetworkMessage):
    questType:int
    availableRetryCount:int
    

    def init(self, questType:int, availableRetryCount:int):
        self.questType = questType
        self.availableRetryCount = availableRetryCount
        
        super().__init__()
    
    