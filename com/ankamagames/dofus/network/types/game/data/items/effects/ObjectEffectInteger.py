from com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffect import ObjectEffect


class ObjectEffectInteger(ObjectEffect):
    value:int
    

    def init(self, value:int, actionId:int):
        self.value = value
        
        super().__init__(actionId)
    
    