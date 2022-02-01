from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class FriendSpouseFollowWithCompassRequestMessage(INetworkMessage):
    protocolId = 8825
    enable:bool
    
    
