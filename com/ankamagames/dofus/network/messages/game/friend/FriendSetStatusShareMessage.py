from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class FriendSetStatusShareMessage(NetworkMessage):
    protocolId = 1404
    share:bool
    
    
