from com.ankamagames.dofus.network.types.game.actions.fight.AbstractFightDispellableEffect import AbstractFightDispellableEffect


class FightTemporarySpellImmunityEffect(AbstractFightDispellableEffect):
    immuneSpellId:int
    

    def init(self, immuneSpellId:int, uid:int, targetId:int, turnDuration:int, dispelable:int, spellId:int, effectId:int, parentBoostUid:int):
        self.immuneSpellId = immuneSpellId
        
        super().__init__(uid, targetId, turnDuration, dispelable, spellId, effectId, parentBoostUid)
    
    