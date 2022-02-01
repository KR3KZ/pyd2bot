from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class SymbioticObjectAssociateRequestMessage(NetworkMessage):
    symbioteUID:int
    symbiotePos:int
    hostUID:int
    hostPos:int
    
    
