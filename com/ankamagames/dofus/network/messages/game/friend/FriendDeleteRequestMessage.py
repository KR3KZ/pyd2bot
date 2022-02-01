from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class FriendDeleteRequestMessage(INetworkMessage):
    protocolId = 7400
    accountId:int
    
    
