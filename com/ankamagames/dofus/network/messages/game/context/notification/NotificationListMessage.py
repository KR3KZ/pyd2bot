from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class NotificationListMessage(NetworkMessage):
    protocolId = 7026
    flags:int
    
    
