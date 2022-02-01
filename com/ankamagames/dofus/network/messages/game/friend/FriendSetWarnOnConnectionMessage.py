from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class FriendSetWarnOnConnectionMessage(INetworkMessage):
    protocolId = 6228
    enable:bool
    
    
