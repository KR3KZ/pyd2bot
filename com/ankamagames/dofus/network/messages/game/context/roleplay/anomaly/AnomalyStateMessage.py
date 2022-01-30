from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class AnomalyStateMessage(NetworkMessage):
    protocolId = 4879
    subAreaId:int
    open:bool
    closingTime:int
    
    
