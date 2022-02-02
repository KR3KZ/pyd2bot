from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.common.AccountTagInformation import AccountTagInformation


@dataclass
class AcquaintanceSearchMessage(NetworkMessage):
    tag:AccountTagInformation
    
    
    def __post_init__(self):
        super().__init__()
    