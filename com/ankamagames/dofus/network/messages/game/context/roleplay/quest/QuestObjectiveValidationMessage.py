from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class QuestObjectiveValidationMessage(INetworkMessage):
    protocolId = 7368
    questId:int
    objectiveId:int
    
    
