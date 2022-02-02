from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.quest.QuestActiveInformations import QuestActiveInformations


@dataclass
class QuestListMessage(NetworkMessage):
    finishedQuestsIds:list[int]
    finishedQuestsCounts:list[int]
    activeQuests:list[QuestActiveInformations]
    reinitDoneQuestsIds:list[int]
    
    
    def __post_init__(self):
        super().__init__()
    