from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.context.roleplay.ObjectItemInRolePlay import ObjectItemInRolePlay
from com.ankamagames.dofus.network.types.game.mount.ItemDurability import ItemDurability


@dataclass
class PaddockItem(ObjectItemInRolePlay):
    durability:ItemDurability
    
    
    def __post_init__(self):
        super().__init__()
    