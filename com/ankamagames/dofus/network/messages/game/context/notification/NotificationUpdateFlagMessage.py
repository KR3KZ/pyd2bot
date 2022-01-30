from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class NotificationUpdateFlagMessage(INetworkMessage):
    protocolId = 8604
    index:int
    
    
