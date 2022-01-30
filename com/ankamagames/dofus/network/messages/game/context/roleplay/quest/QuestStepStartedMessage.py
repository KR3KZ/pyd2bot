from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class QuestStepStartedMessage(INetworkMessage):
    protocolId = 6142
    questId:int
    stepId:int
    
    
