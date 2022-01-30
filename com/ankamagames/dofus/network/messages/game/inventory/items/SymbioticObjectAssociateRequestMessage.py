from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class SymbioticObjectAssociateRequestMessage(NetworkMessage):
    protocolId = 7604
    symbioteUID:int
    symbiotePos:int
    hostUID:int
    hostPos:int
    
