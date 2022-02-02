from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffect import ObjectEffect
from com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffectInteger import ObjectEffectInteger


@dataclass
class ObjectEffectMount(ObjectEffect):
    id:int
    expirationDate:int
    model:int
    name:str
    owner:str
    level:int
    reproductionCount:int
    reproductionCountMax:int
    effects:list[ObjectEffectInteger]
    capacities:list[int]
    sex:bool
    isRideable:bool
    isFeconded:bool
    isFecondationReady:bool
    
    
    def __post_init__(self):
        super().__init__()
    