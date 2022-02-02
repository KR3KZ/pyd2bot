from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.data.items.Item import Item
from com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffect import ObjectEffect


@dataclass
class ObjectItemMinimalInformation(Item):
    objectGID:int
    effects:list[ObjectEffect]
    
    
    def __post_init__(self):
        super().__init__()
    