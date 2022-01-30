from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class FriendWarnOnConnectionStateMessage(NetworkMessage):
    protocolId = 6412
    enable:bool
    
