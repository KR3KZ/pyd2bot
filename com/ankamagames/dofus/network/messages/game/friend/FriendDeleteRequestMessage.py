from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class FriendDeleteRequestMessage(INetworkMessage):
    protocolId = 7400
    accountId:int
    
    
