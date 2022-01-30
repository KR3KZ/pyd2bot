from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class FriendAddFailureMessage(INetworkMessage):
    protocolId = 4074
    reason:int
    
    
