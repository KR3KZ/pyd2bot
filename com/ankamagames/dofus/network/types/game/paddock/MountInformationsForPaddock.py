from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class MountInformationsForPaddock(NetworkMessage):
    modelId:int
    name:str
    ownerName:str
    
    
    def __post_init__(self):
        super().__init__()
    