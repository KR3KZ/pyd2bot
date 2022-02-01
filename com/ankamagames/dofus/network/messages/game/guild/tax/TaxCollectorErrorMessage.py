from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class TaxCollectorErrorMessage(INetworkMessage):
    protocolId = 4836
    reason:int
    
    
