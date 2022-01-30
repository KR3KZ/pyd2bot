from com.ankamagames.dofus.network.messages.game.context.roleplay.quest.QuestStepInfoRequestMessage import QuestStepInfoRequestMessage


class WatchQuestStepInfoRequestMessage(QuestStepInfoRequestMessage):
    protocolId = 8640
    playerId:int
    
    
