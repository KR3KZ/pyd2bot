from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class TaxCollectorMovementRemoveMessage(NetworkMessage):
    protocolId = 5927
    collectorId:int
    
