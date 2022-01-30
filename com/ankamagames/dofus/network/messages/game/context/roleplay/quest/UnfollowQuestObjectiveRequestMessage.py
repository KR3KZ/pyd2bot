from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class UnfollowQuestObjectiveRequestMessage(INetworkMessage):
    protocolId = 3466
    questId:int
    objectiveId:int
    
    
