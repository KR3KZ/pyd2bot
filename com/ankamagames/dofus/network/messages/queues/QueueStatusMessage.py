from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class QueueStatusMessage(NetworkMessage):
    protocolId = 2197
    position:int
    total:int
    
    
