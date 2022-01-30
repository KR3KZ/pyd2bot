from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class FriendSpouseFollowWithCompassRequestMessage(NetworkMessage):
    protocolId = 8825
    enable:bool
    
