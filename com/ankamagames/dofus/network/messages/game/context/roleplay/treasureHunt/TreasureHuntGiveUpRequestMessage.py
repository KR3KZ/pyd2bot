from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class TreasureHuntGiveUpRequestMessage(NetworkMessage):
    questType:int
    

    def init(self, questType:int):
        self.questType = questType
        
        super().__init__()
    
    