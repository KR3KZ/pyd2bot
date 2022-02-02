from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class WrapperObjectDissociateRequestMessage(NetworkMessage):
    hostUID:int
    hostPos:int
    
    
    def __post_init__(self):
        super().__init__()
    