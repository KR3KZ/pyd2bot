from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class FriendSetStatusShareMessage(INetworkMessage):
    protocolId = 1404
    share:bool
    
    
