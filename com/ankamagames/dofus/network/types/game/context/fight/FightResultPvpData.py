from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.context.fight.FightResultAdditionalData import FightResultAdditionalData


@dataclass
class FightResultPvpData(FightResultAdditionalData):
    grade:int
    minHonorForGrade:int
    maxHonorForGrade:int
    honor:int
    honorDelta:int
    
    
    def __post_init__(self):
        super().__init__()
    