from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class AbstractFightDispellableEffect(INetworkMessage):
    protocolId = 1657
    uid:int
    targetId:int
    turnDuration:int
    dispelable:int
    spellId:int
    effectId:int
    parentBoostUid:int
    
    
