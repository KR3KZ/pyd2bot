from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class FriendSetStatusShareMessage(INetworkMessage):
    protocolId = 1404
    share:bool
    
    
