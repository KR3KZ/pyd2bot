from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class QuestStepInfoRequestMessage(NetworkMessage):
    questId:int
    

    def init(self, questId:int):
        self.questId = questId
        
        super().__init__()
    
    