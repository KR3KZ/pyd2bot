from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class PrismSetSabotagedRefusedMessage(INetworkMessage):
    protocolId = 5200
    subAreaId:int
    reason:int
    
    
