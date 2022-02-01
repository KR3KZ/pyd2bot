from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class UnfollowQuestObjectiveRequestMessage(NetworkMessage):
    questId:int
    objectiveId:int
    
    
