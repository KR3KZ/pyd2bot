from com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffect import ObjectEffect


class ObjectEffectMinMax(ObjectEffect):
    min:int
    max:int
    

    def init(self, min:int, max:int, actionId:int):
        self.min = min
        self.max = max
        
        super().__init__(actionId)
    
    