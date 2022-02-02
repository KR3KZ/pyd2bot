from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.friend.IgnoredInformations import IgnoredInformations


@dataclass
class IgnoredOnlineInformations(IgnoredInformations):
    playerId:int
    playerName:str
    breed:int
    sex:bool
    
    
    def __post_init__(self):
        super().__init__()
    