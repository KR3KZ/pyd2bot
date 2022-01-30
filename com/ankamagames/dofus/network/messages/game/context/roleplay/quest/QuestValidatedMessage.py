from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class QuestValidatedMessage(NetworkMessage):
    protocolId = 1984
    questId:int
    
    
