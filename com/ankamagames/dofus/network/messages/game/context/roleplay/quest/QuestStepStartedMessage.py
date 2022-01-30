from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class QuestStepStartedMessage(NetworkMessage):
    protocolId = 6142
    questId:int
    stepId:int
    
    
