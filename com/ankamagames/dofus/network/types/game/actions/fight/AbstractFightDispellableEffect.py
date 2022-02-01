from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class AbstractFightDispellableEffect(NetworkMessage):
    uid:int
    targetId:int
    turnDuration:int
    dispelable:int
    spellId:int
    effectId:int
    parentBoostUid:int
    
    
