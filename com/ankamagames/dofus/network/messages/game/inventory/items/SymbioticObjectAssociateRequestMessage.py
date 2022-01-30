from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class SymbioticObjectAssociateRequestMessage(INetworkMessage):
    protocolId = 7604
    symbioteUID:int
    symbiotePos:int
    hostUID:int
    hostPos:int
    
    
