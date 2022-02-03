from com.ankamagames.dofus.network.types.game.context.roleplay.quest.QuestObjectiveInformations import QuestObjectiveInformations


class QuestObjectiveInformationsWithCompletion(QuestObjectiveInformations):
    curCompletion:int
    maxCompletion:int
    

    def init(self, curCompletion:int, maxCompletion:int, objectiveId:int, objectiveStatus:bool, dialogParams:list[str]):
        self.curCompletion = curCompletion
        self.maxCompletion = maxCompletion
        
        super().__init__(objectiveId, objectiveStatus, dialogParams)
    
    