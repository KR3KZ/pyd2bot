from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class AbstractFightDispellableEffect(INetworkMessage):
    protocolId = 1657
    uid:int
    targetId:int
    turnDuration:int
    dispelable:int
    spellId:int
    effectId:int
    parentBoostUid:int
    
    
