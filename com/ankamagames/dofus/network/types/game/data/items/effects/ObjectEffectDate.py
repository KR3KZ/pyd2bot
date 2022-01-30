from com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffect import ObjectEffect


class ObjectEffectDate(ObjectEffect):
    protocolId = 5415
    year:int
    month:int
    day:int
    hour:int
    minute:int
    
    
