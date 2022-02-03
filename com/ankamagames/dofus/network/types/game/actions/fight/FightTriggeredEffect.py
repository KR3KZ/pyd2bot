from com.ankamagames.dofus.network.types.game.actions.fight.AbstractFightDispellableEffect import AbstractFightDispellableEffect


class FightTriggeredEffect(AbstractFightDispellableEffect):
    param1:int
    param2:int
    param3:int
    delay:int
    

    def init(self, param1:int, param2:int, param3:int, delay:int, uid:int, targetId:int, turnDuration:int, dispelable:int, spellId:int, effectId:int, parentBoostUid:int):
        self.param1 = param1
        self.param2 = param2
        self.param3 = param3
        self.delay = delay
        
        super().__init__(uid, targetId, turnDuration, dispelable, spellId, effectId, parentBoostUid)
    
    