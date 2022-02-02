from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.context.fight.FightResultFighterListEntry import FightResultFighterListEntry


@dataclass
class FightResultMutantListEntry(FightResultFighterListEntry):
    level:int
    
    
    def __post_init__(self):
        super().__init__()
    