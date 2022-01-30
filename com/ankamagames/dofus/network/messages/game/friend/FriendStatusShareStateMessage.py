from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class FriendStatusShareStateMessage(NetworkMessage):
    protocolId = 433
    share:bool
    
