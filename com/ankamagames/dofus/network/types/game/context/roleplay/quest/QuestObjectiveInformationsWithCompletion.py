from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.context.roleplay.quest.QuestObjectiveInformations import QuestObjectiveInformations


@dataclass
class QuestObjectiveInformationsWithCompletion(QuestObjectiveInformations):
    curCompletion:int
    maxCompletion:int
    
    
    def __post_init__(self):
        super().__init__()
    