from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class QuestObjectiveInformations(NetworkMessage):
    protocolId = 4677
    objectiveId:int
    objectiveStatus:bool
    dialogParams:list[str]
    
