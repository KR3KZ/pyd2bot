from com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffect import ObjectEffect
from com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffectInteger import ObjectEffectInteger


class ObjectEffectMount(ObjectEffect):
    protocolId = 4916
    id:int
    expirationDate:int
    model:int
    name:str
    owner:str
    level:int
    reproductionCount:int
    reproductionCountMax:int
    effects:ObjectEffectInteger
    capacities:int
    
