from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class FollowQuestObjectiveRequestMessage(INetworkMessage):
    protocolId = 8182
    questId:int
    objectiveId:int
    
    
