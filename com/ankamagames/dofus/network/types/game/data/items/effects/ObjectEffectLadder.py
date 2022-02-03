from com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffectCreature import ObjectEffectCreature


class ObjectEffectLadder(ObjectEffectCreature):
    monsterCount:int
    

    def init(self, monsterCount:int, monsterFamilyId:int, actionId:int):
        self.monsterCount = monsterCount
        
        super().__init__(monsterFamilyId, actionId)
    
    