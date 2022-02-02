from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffect import ObjectEffect


@dataclass
class ObjectEffectString(ObjectEffect):
    value:str
    
    
    def __post_init__(self):
        super().__init__()
    