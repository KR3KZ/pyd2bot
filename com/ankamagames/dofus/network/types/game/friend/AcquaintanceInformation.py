from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.friend.AbstractContactInformations import AbstractContactInformations


@dataclass
class AcquaintanceInformation(AbstractContactInformations):
    playerState:int
    
    
    def __post_init__(self):
        super().__init__()
    