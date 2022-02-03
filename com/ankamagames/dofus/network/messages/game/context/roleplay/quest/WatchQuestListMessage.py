from com.ankamagames.dofus.network.messages.game.context.roleplay.quest.QuestListMessage import QuestListMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.quest.QuestActiveInformations import QuestActiveInformations
    


class WatchQuestListMessage(QuestListMessage):
    playerId:int
    

    def init(self, playerId:int, finishedQuestsIds:list[int], finishedQuestsCounts:list[int], activeQuests:list['QuestActiveInformations'], reinitDoneQuestsIds:list[int]):
        self.playerId = playerId
        
        super().__init__(finishedQuestsIds, finishedQuestsCounts, activeQuests, reinitDoneQuestsIds)
    
    