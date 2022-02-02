from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffect import ObjectEffect


@dataclass
class ObjectEffectDuration(ObjectEffect):
    days:int
    hours:int
    minutes:int
    
    
    def __post_init__(self):
        super().__init__()
    