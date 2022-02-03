from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class QuestObjectiveValidationMessage(NetworkMessage):
    questId:int
    objectiveId:int
    

    def init(self, questId:int, objectiveId:int):
        self.questId = questId
        self.objectiveId = objectiveId
        
        super().__init__()
    
    