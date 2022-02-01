from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class QuestStepValidatedMessage(INetworkMessage):
    protocolId = 6173
    questId:int
    stepId:int
    
    
