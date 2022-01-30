from com.ankamagames.dofus.network.messages.game.context.roleplay.quest.QuestStepInfoMessage import QuestStepInfoMessage


class WatchQuestStepInfoMessage(QuestStepInfoMessage):
    protocolId = 2727
    playerId:int
    
