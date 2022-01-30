from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class TaxCollectorStateUpdateMessage(INetworkMessage):
    protocolId = 7095
    uniqueId:int
    state:int
    
    
