from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class TaxCollectorMovementRemoveMessage(INetworkMessage):
    protocolId = 5927
    collectorId:int
    
    
