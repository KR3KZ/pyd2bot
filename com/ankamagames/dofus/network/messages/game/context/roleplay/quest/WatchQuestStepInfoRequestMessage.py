from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.context.roleplay.quest.QuestStepInfoRequestMessage import QuestStepInfoRequestMessage


@dataclass
class WatchQuestStepInfoRequestMessage(QuestStepInfoRequestMessage):
    playerId:int
    
    
    def __post_init__(self):
        super().__init__()
    