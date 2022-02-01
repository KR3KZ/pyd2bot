from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class TaxCollectorMovementRemoveMessage(INetworkMessage):
    protocolId = 5927
    collectorId:int
    
    
