from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class FriendSetWarnOnConnectionMessage(INetworkMessage):
    protocolId = 6228
    enable:bool
    
    
