from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class FriendAddFailureMessage(INetworkMessage):
    protocolId = 4074
    reason:int
    
    
