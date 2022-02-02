from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.context.roleplay.quest.QuestActiveInformations import QuestActiveInformations
from com.ankamagames.dofus.network.types.game.context.roleplay.quest.QuestObjectiveInformations import QuestObjectiveInformations


@dataclass
class QuestActiveDetailedInformations(QuestActiveInformations):
    stepId:int
    objectives:list[QuestObjectiveInformations]
    
    
    def __post_init__(self):
        super().__init__()
    