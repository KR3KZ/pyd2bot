from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.context.roleplay.HumanOption import HumanOption
from com.ankamagames.dofus.network.types.game.look.IndexedEntityLook import IndexedEntityLook


@dataclass
class HumanOptionFollowers(HumanOption):
    followingCharactersLook:list[IndexedEntityLook]
    
    
    def __post_init__(self):
        super().__init__()
    