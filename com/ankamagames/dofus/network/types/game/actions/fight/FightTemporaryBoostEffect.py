from com.ankamagames.dofus.network.types.game.actions.fight.AbstractFightDispellableEffect import AbstractFightDispellableEffect


class FightTemporaryBoostEffect(AbstractFightDispellableEffect):
    delta:int
    

    def init(self, delta:int, uid:int, targetId:int, turnDuration:int, dispelable:int, spellId:int, effectId:int, parentBoostUid:int):
        self.delta = delta
        
        super().__init__(uid, targetId, turnDuration, dispelable, spellId, effectId, parentBoostUid)
    
    