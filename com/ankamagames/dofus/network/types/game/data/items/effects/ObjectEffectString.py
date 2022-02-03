from com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffect import ObjectEffect


class ObjectEffectString(ObjectEffect):
    value:str
    

    def init(self, value:str, actionId:int):
        self.value = value
        
        super().__init__(actionId)
    
    