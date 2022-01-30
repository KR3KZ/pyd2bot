from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class FriendSpouseFollowWithCompassRequestMessage(INetworkMessage):
    protocolId = 8825
    enable:bool
    
    
