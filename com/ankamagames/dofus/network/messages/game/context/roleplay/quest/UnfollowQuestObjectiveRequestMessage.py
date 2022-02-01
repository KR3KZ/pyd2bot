from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class UnfollowQuestObjectiveRequestMessage(INetworkMessage):
    protocolId = 3466
    questId:int
    objectiveId:int
    
    
