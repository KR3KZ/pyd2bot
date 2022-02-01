from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class QuestObjectiveValidatedMessage(INetworkMessage):
    protocolId = 5565
    questId:int
    objectiveId:int
    
    
