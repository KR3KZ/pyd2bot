from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.context.roleplay.quest.QuestListMessage import QuestListMessage


@dataclass
class WatchQuestListMessage(QuestListMessage):
    playerId:int
    
    
    def __post_init__(self):
        super().__init__()
    