from com.ankamagames.dofus.network.types.game.context.roleplay.quest.QuestObjectiveInformations import QuestObjectiveInformations


class QuestObjectiveInformationsWithCompletion(QuestObjectiveInformations):
    protocolId = 5115
    curCompletion:int
    maxCompletion:int
    
