from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class QuestObjectiveValidationMessage(INetworkMessage):
    protocolId = 7368
    questId:int
    objectiveId:int
    
    
