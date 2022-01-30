from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class OnConnectionEventMessage(NetworkMessage):
    protocolId = 4485
    eventType:int
    
