from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffect import ObjectEffect


@dataclass
class ObjectEffectDate(ObjectEffect):
    year:int
    month:int
    day:int
    hour:int
    minute:int
    
    
    def __post_init__(self):
        super().__init__()
    