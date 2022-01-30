from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class CurrentServerStatusUpdateMessage(NetworkMessage):
    protocolId = 547
    status:int
    
    
