from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class UnfollowQuestObjectiveRequestMessage(NetworkMessage):
    protocolId = 3466
    questId:int
    objectiveId:int
    
