from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class FollowQuestObjectiveRequestMessage(INetworkMessage):
    protocolId = 8182
    questId:int
    objectiveId:int
    
    
