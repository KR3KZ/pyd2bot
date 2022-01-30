from com.ankamagames.dofus.network.types.game.data.items.Item import Item
from com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffect import ObjectEffect


class ObjectItemToSellInHumanVendorShop(Item):
    protocolId = 3057
    objectGID:int
    effects:ObjectEffect
    objectUID:int
    quantity:int
    objectPrice:int
    publicPrice:int
    
