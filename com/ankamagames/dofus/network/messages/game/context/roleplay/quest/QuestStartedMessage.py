from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class QuestStartedMessage(NetworkMessage):
    questId:int
    

    def init(self, questId:int):
        self.questId = questId
        
        super().__init__()
    
    