from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class PrismSetSabotagedRefusedMessage(NetworkMessage):
    protocolId = 5200
    subAreaId:int
    reason:int
    
