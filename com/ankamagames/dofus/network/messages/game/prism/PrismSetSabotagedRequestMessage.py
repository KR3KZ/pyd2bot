from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class PrismSetSabotagedRequestMessage(INetworkMessage):
    protocolId = 1746
    subAreaId:int
    
    
