from dataclasses import dataclass
from com.ankamagames.dofus.network.types.common.AbstractPlayerSearchInformation import AbstractPlayerSearchInformation
from com.ankamagames.dofus.network.types.common.AccountTagInformation import AccountTagInformation


@dataclass
class PlayerSearchTagInformation(AbstractPlayerSearchInformation):
    tag:AccountTagInformation
    
    
    def __post_init__(self):
        super().__init__()
    