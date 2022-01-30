from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class QuestStepInfoRequestMessage(NetworkMessage):
    protocolId = 5562
    questId:int
    
    
