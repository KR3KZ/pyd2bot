from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class TaxCollectorStateUpdateMessage(INetworkMessage):
    protocolId = 7095
    uniqueId:int
    state:int
    
    
