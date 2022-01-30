from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class QuestStepValidatedMessage(NetworkMessage):
    protocolId = 6173
    questId:int
    stepId:int
    
