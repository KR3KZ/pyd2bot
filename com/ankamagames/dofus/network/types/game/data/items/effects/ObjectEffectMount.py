from com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffect import ObjectEffect
from com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffectInteger import ObjectEffectInteger


class ObjectEffectMount(ObjectEffect):
    protocolId = 4916
    id:float
    expirationDate:float
    model:int
    name:str
    owner:str
    level:int
    reproductionCount:int
    reproductionCountMax:int
    effects:list[ObjectEffectInteger]
    capacities:list[int]
    
