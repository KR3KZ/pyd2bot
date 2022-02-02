from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.character.status.PlayerStatus import PlayerStatus


@dataclass
class PlayerStatusExtended(PlayerStatus):
    message:str
    
    
    def __post_init__(self):
        super().__init__()
    