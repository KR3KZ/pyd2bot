from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.common.AccountTagInformation import AccountTagInformation


@dataclass
class IgnoredDeleteResultMessage(NetworkMessage):
    tag:AccountTagInformation
    success:bool
    session:bool
    
    
    def __post_init__(self):
        super().__init__()
    