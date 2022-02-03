from com.ankamagames.dofus.network.types.game.actions.fight.FightTemporaryBoostEffect import FightTemporaryBoostEffect


class FightTemporarySpellBoostEffect(FightTemporaryBoostEffect):
    boostedSpellId:int
    

    def init(self, boostedSpellId:int, delta:int, uid:int, targetId:int, turnDuration:int, dispelable:int, spellId:int, effectId:int, parentBoostUid:int):
        self.boostedSpellId = boostedSpellId
        
        super().__init__(delta, uid, targetId, turnDuration, dispelable, spellId, effectId, parentBoostUid)
    
    