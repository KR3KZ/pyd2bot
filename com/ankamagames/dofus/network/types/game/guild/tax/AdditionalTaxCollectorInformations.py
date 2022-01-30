from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class AdditionalTaxCollectorInformations(INetworkMessage):
    protocolId = 9432
    collectorCallerName:str
    date:int
    
    
