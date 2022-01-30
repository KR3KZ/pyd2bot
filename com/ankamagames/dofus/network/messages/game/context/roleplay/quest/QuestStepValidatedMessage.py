from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class QuestStepValidatedMessage(INetworkMessage):
    protocolId = 6173
    questId:int
    stepId:int
    
    
