from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.quest.QuestActiveInformations import QuestActiveInformations


class QuestListMessage(NetworkMessage):
    finishedQuestsIds:list[int]
    finishedQuestsCounts:list[int]
    activeQuests:list[QuestActiveInformations]
    reinitDoneQuestsIds:list[int]
    
    
