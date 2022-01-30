from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class QueueStatusMessage(INetworkMessage):
    protocolId = 2197
    position:int
    total:int
    
    
