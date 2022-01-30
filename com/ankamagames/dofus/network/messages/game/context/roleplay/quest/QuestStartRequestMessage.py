from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class QuestStartRequestMessage(NetworkMessage):
    protocolId = 6071
    questId:int
    
    
