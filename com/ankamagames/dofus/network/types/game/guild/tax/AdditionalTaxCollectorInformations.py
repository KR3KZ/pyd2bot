from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class AdditionalTaxCollectorInformations(INetworkMessage):
    protocolId = 9432
    collectorCallerName:str
    date:int
    
    
