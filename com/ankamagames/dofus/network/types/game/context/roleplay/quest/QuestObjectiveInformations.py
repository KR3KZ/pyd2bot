from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class QuestObjectiveInformations(INetworkMessage):
    protocolId = 4677
    objectiveId:int
    objectiveStatus:bool
    dialogParams:str
    
    
