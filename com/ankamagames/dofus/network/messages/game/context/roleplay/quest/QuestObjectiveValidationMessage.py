from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class QuestObjectiveValidationMessage(NetworkMessage):
    protocolId = 7368
    questId:int
    objectiveId:int
    
