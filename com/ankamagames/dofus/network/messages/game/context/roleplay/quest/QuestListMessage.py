from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.quest.QuestActiveInformations import QuestActiveInformations


class QuestListMessage(INetworkMessage):
    protocolId = 5774
    finishedQuestsIds:int
    finishedQuestsCounts:int
    activeQuests:QuestActiveInformations
    reinitDoneQuestsIds:int
    
    
