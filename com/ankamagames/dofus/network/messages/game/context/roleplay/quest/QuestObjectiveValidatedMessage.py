from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class QuestObjectiveValidatedMessage(INetworkMessage):
    protocolId = 5565
    questId:int
    objectiveId:int
    
    
