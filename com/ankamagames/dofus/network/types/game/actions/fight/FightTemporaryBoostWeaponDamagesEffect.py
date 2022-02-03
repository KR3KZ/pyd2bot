from com.ankamagames.dofus.network.types.game.actions.fight.FightTemporaryBoostEffect import FightTemporaryBoostEffect


class FightTemporaryBoostWeaponDamagesEffect(FightTemporaryBoostEffect):
    weaponTypeId:int
    

    def init(self, weaponTypeId:int, delta:int, uid:int, targetId:int, turnDuration:int, dispelable:int, spellId:int, effectId:int, parentBoostUid:int):
        self.weaponTypeId = weaponTypeId
        
        super().__init__(delta, uid, targetId, turnDuration, dispelable, spellId, effectId, parentBoostUid)
    
    