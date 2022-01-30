from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class FriendAddFailureMessage(NetworkMessage):
    protocolId = 4074
    reason:int
    
