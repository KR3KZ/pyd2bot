from com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffect import ObjectEffect


class ObjectEffectCreature(ObjectEffect):
    monsterFamilyId:int
    

    def init(self, monsterFamilyId:int, actionId:int):
        self.monsterFamilyId = monsterFamilyId
        
        super().__init__(actionId)
    
    