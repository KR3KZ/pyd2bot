from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class OnConnectionEventMessage(INetworkMessage):
    protocolId = 4485
    eventType:int
    
    
