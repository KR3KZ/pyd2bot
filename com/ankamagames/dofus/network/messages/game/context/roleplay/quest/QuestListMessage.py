from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.quest.QuestActiveInformations import QuestActiveInformations


class QuestListMessage(NetworkMessage):
    protocolId = 5774
    finishedQuestsIds:int
    finishedQuestsCounts:int
    activeQuests:QuestActiveInformations
    reinitDoneQuestsIds:int
    
    
