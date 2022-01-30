from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class LoginQueueStatusMessage(NetworkMessage):
    protocolId = 2063
    position:int
    total:int
    
    
