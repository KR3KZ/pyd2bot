from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class SymbioticObjectAssociateRequestMessage(NetworkMessage):
    symbioteUID:int
    symbiotePos:int
    hostUID:int
    hostPos:int
    
    
    def __post_init__(self):
        super().__init__()
    