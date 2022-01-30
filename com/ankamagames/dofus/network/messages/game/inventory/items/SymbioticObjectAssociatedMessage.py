from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class SymbioticObjectAssociatedMessage(NetworkMessage):
    protocolId = 4986
    hostUID:int
    
