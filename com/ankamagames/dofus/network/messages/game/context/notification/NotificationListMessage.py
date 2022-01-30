from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class NotificationListMessage(INetworkMessage):
    protocolId = 7026
    flags:int
    
    
