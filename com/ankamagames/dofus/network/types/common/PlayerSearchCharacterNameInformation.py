from dataclasses import dataclass
from com.ankamagames.dofus.network.types.common.AbstractPlayerSearchInformation import AbstractPlayerSearchInformation


@dataclass
class PlayerSearchCharacterNameInformation(AbstractPlayerSearchInformation):
    name:str
    
    
    def __post_init__(self):
        super().__init__()
    