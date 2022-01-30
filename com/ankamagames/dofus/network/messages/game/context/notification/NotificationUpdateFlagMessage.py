from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class NotificationUpdateFlagMessage(NetworkMessage):
    protocolId = 8604
    index:int
    
    
