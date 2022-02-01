from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class SymbioticObjectAssociateRequestMessage(INetworkMessage):
    protocolId = 7604
    symbioteUID:int
    symbiotePos:int
    hostUID:int
    hostPos:int
    
    
