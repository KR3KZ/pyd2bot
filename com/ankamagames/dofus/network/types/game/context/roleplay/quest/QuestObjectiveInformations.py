from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class QuestObjectiveInformations(NetworkMessage):
    objectiveId:int
    objectiveStatus:bool
    dialogParams:list[str]
    
    
