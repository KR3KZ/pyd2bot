from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class AbstractFightDispellableEffect(NetworkMessage):
    uid:int
    targetId:int
    turnDuration:int
    dispelable:int
    spellId:int
    effectId:int
    parentBoostUid:int
    

    def init(self, uid:int, targetId:int, turnDuration:int, dispelable:int, spellId:int, effectId:int, parentBoostUid:int):
        self.uid = uid
        self.targetId = targetId
        self.turnDuration = turnDuration
        self.dispelable = dispelable
        self.spellId = spellId
        self.effectId = effectId
        self.parentBoostUid = parentBoostUid
        
        super().__init__()
    
    