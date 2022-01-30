from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class AnomalyStateMessage(INetworkMessage):
    protocolId = 4879
    subAreaId:int
    open:bool
    closingTime:int
    
    
