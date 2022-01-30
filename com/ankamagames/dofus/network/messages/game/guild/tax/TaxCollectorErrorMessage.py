from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class TaxCollectorErrorMessage(NetworkMessage):
    protocolId = 4836
    reason:int
    
    
