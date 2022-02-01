from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class QuestStepStartedMessage(INetworkMessage):
    protocolId = 6142
    questId:int
    stepId:int
    
    
