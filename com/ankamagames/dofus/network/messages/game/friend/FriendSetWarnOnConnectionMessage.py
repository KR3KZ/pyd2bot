from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class FriendSetWarnOnConnectionMessage(NetworkMessage):
    protocolId = 6228
    enable:bool
    
    
