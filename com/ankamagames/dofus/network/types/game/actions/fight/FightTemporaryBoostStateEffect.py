from com.ankamagames.dofus.network.types.game.actions.fight.FightTemporaryBoostEffect import FightTemporaryBoostEffect


class FightTemporaryBoostStateEffect(FightTemporaryBoostEffect):
    stateId:int
    

    def init(self, stateId:int, delta:int, uid:int, targetId:int, turnDuration:int, dispelable:int, spellId:int, effectId:int, parentBoostUid:int):
        self.stateId = stateId
        
        super().__init__(delta, uid, targetId, turnDuration, dispelable, spellId, effectId, parentBoostUid)
    
    