from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class QuestObjectiveValidationMessage(NetworkMessage):
    questId:int
    objectiveId:int
    
    
