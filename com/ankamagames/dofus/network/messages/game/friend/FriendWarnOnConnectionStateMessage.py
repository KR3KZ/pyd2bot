from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class FriendWarnOnConnectionStateMessage(INetworkMessage):
    protocolId = 6412
    enable:bool
    
    
