from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.idol.Idol import Idol


@dataclass
class PartyIdol(Idol):
    ownersIds:list[int]
    
    
    def __post_init__(self):
        super().__init__()
    