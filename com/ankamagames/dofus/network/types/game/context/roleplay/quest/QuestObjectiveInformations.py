from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class QuestObjectiveInformations(INetworkMessage):
    protocolId = 4677
    objectiveId:int
    objectiveStatus:bool
    dialogParams:str
    
    
