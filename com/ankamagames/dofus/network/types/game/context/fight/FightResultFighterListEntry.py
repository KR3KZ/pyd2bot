from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.context.fight.FightResultListEntry import FightResultListEntry


@dataclass
class FightResultFighterListEntry(FightResultListEntry):
    id:int
    alive:bool
    
    
    def __post_init__(self):
        super().__init__()
    