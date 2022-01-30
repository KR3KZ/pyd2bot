from com.ankamagames.dofus.network.types.game.data.items.Item import Item
from com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffect import ObjectEffect


class ObjectItemNotInContainer(Item):
    protocolId = 8362
    objectGID:int
    effects:ObjectEffect
    objectUID:int
    quantity:int
    
    
