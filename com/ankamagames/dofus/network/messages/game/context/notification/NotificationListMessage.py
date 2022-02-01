from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class NotificationListMessage(INetworkMessage):
    protocolId = 7026
    flags:int
    
    
