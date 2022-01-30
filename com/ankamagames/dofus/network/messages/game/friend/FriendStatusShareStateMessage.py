from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class FriendStatusShareStateMessage(INetworkMessage):
    protocolId = 433
    share:bool
    
    
