from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class PrismSetSabotagedRequestMessage(NetworkMessage):
    protocolId = 1746
    subAreaId:int
    
    
