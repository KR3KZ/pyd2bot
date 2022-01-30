from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ChatErrorMessage(NetworkMessage):
    protocolId = 5479
    reason:int
    
