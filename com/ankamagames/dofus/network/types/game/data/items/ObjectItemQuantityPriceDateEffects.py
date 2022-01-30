from com.ankamagames.dofus.network.types.game.data.items.ObjectItemGenericQuantity import ObjectItemGenericQuantity
from com.ankamagames.dofus.network.types.game.data.items.ObjectEffects import ObjectEffects


class ObjectItemQuantityPriceDateEffects(ObjectItemGenericQuantity):
    protocolId = 7217
    price:int
    effects:ObjectEffects
    date:int
    
