from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class FollowQuestObjectiveRequestMessage(NetworkMessage):
    questId:int
    objectiveId:int
    
    
