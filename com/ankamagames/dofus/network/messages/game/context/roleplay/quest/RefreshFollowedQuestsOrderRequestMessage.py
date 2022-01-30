from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class RefreshFollowedQuestsOrderRequestMessage(NetworkMessage):
    protocolId = 1088
    quests:int
    
