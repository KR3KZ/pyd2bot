from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.common.AbstractPlayerSearchInformation import AbstractPlayerSearchInformation


@dataclass
class IgnoredAddRequestMessage(NetworkMessage):
    target:AbstractPlayerSearchInformation
    session:bool
    
    
    def __post_init__(self):
        super().__init__()
    