from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class FollowQuestObjectiveRequestMessage(NetworkMessage):
    protocolId = 8182
    questId:int
    objectiveId:int
    
