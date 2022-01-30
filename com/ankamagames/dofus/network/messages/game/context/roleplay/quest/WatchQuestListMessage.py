from com.ankamagames.dofus.network.messages.game.context.roleplay.quest.QuestListMessage import QuestListMessage


class WatchQuestListMessage(QuestListMessage):
    protocolId = 9128
    playerId:float
    
