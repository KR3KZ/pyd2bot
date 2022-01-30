from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class MountDataErrorMessage(NetworkMessage):
    protocolId = 24
    reason:int
    
    
