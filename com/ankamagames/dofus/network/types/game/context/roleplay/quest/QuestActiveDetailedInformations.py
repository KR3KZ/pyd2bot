from com.ankamagames.dofus.network.types.game.context.roleplay.quest.QuestActiveInformations import QuestActiveInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.quest.QuestObjectiveInformations import QuestObjectiveInformations
    


class QuestActiveDetailedInformations(QuestActiveInformations):
    stepId:int
    objectives:list['QuestObjectiveInformations']
    

    def init(self, stepId:int, objectives:list['QuestObjectiveInformations'], questId:int):
        self.stepId = stepId
        self.objectives = objectives
        
        super().__init__(questId)
    
    