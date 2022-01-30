from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class IgnoredAddFailureMessage(NetworkMessage):
    protocolId = 4052
    reason:int
    
    
