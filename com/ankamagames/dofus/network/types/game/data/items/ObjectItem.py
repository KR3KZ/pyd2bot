from com.ankamagames.dofus.network.types.game.data.items.Item import Item
from com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffect import ObjectEffect


class ObjectItem(Item):
    protocolId = 2916
    position:int
    objectGID:int
    effects:ObjectEffect
    objectUID:int
    quantity:int
    
    
