from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class AdditionalTaxCollectorInformations(NetworkMessage):
    protocolId = 9432
    collectorCallerName:str
    date:int
    
