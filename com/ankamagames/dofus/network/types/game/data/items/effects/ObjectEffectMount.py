from com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffect import ObjectEffect
from com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffectInteger import ObjectEffectInteger


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
    
    
