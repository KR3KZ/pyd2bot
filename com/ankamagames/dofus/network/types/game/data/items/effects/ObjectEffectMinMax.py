from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffect import ObjectEffect


@dataclass
class ObjectEffectMinMax(ObjectEffect):
    min:int
    max:int
    
    
    def __post_init__(self):
        super().__init__()
    