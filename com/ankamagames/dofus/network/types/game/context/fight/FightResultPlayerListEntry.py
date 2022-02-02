from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.context.fight.FightResultFighterListEntry import FightResultFighterListEntry
from com.ankamagames.dofus.network.types.game.context.fight.FightResultAdditionalData import FightResultAdditionalData


@dataclass
class FightResultPlayerListEntry(FightResultFighterListEntry):
    level:int
    additional:list[FightResultAdditionalData]
    
    
    def __post_init__(self):
        super().__init__()
    