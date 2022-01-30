from com.ankamagames.dofus.network.types.game.data.items.Item import Item
from com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffect import ObjectEffect


class ObjectItemMinimalInformation(Item):
    protocolId = 4918
    objectGID:int
    effects:ObjectEffect
    
    
