from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class TreasureHuntDigRequestAnswerMessage(NetworkMessage):
    questType:int
    result:int
    

    def init(self, questType:int, result:int):
        self.questType = questType
        self.result = result
        
        super().__init__()
    
    