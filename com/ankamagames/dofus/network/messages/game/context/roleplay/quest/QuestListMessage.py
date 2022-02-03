from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.quest.QuestActiveInformations import QuestActiveInformations
    


class QuestListMessage(NetworkMessage):
    finishedQuestsIds:list[int]
    finishedQuestsCounts:list[int]
    activeQuests:list['QuestActiveInformations']
    reinitDoneQuestsIds:list[int]
    

    def init(self, finishedQuestsIds:list[int], finishedQuestsCounts:list[int], activeQuests:list['QuestActiveInformations'], reinitDoneQuestsIds:list[int]):
        self.finishedQuestsIds = finishedQuestsIds
        self.finishedQuestsCounts = finishedQuestsCounts
        self.activeQuests = activeQuests
        self.reinitDoneQuestsIds = reinitDoneQuestsIds
        
        super().__init__()
    
    