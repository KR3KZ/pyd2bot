from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ObjectErrorMessage(NetworkMessage):
    protocolId = 9603
    reason:int
    
