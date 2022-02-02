from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.data.items.ObjectItemMinimalInformation import ObjectItemMinimalInformation


@dataclass
class ObjectItemToSellInNpcShop(ObjectItemMinimalInformation):
    objectPrice:int
    buyCriterion:str
    
    
    def __post_init__(self):
        super().__init__()
    