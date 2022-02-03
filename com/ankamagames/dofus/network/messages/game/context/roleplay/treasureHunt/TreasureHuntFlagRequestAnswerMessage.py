from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class TreasureHuntFlagRequestAnswerMessage(NetworkMessage):
    questType:int
    result:int
    index:int
    

    def init(self, questType:int, result:int, index:int):
        self.questType = questType
        self.result = result
        self.index = index
        
        super().__init__()
    
    