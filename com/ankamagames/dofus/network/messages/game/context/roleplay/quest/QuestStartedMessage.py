from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class QuestStartedMessage(NetworkMessage):
    protocolId = 475
    questId:int
    
