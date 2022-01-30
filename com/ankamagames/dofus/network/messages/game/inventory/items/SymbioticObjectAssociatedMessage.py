from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class SymbioticObjectAssociatedMessage(INetworkMessage):
    protocolId = 4986
    hostUID:int
    
    
