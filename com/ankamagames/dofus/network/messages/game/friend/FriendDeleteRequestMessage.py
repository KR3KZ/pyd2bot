from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class FriendDeleteRequestMessage(NetworkMessage):
    protocolId = 7400
    accountId:int
    
    
