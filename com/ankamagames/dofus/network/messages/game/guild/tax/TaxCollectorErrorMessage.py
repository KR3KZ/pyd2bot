from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class TaxCollectorErrorMessage(INetworkMessage):
    protocolId = 4836
    reason:int
    
    
