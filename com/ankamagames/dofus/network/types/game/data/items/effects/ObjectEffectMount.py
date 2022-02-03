from com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffect import ObjectEffect
from typing import TYPE_CHECKING
if TYPE_CHECKING:
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
    effects:list['ObjectEffectInteger']
    capacities:list[int]
    sex:bool
    isRideable:bool
    isFeconded:bool
    isFecondationReady:bool
    

    def init(self, id:int, expirationDate:int, model:int, name:str, owner:str, level:int, reproductionCount:int, reproductionCountMax:int, effects:list['ObjectEffectInteger'], capacities:list[int], actionId:int):
        self.id = id
        self.expirationDate = expirationDate
        self.model = model
        self.name = name
        self.owner = owner
        self.level = level
        self.reproductionCount = reproductionCount
        self.reproductionCountMax = reproductionCountMax
        self.effects = effects
        self.capacities = capacities
        
        super().__init__(actionId)
    
    