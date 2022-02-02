from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.context.EntityDispositionInformations import EntityDispositionInformations


@dataclass
class FightEntityDispositionInformations(EntityDispositionInformations):
    carryingCharacterId:int
    
    
    def __post_init__(self):
        super().__init__()
    