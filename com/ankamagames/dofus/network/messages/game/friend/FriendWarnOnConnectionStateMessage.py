from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class FriendWarnOnConnectionStateMessage(INetworkMessage):
    protocolId = 6412
    enable:bool
    
    
