from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class QuestObjectiveValidatedMessage(NetworkMessage):
    protocolId = 5565
    questId:int
    objectiveId:int
    
    
