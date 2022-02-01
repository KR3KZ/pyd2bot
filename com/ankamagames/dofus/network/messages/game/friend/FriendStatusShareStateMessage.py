from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class FriendStatusShareStateMessage(INetworkMessage):
    protocolId = 433
    share:bool
    
    
