from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class NotificationUpdateFlagMessage(INetworkMessage):
    protocolId = 8604
    index:int
    
    
