from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class QuestActiveInformations(NetworkMessage):
    protocolId = 1975
    questId:int
    
    
