from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class CurrentServerStatusUpdateMessage(INetworkMessage):
    protocolId = 547
    status:int
    
    
