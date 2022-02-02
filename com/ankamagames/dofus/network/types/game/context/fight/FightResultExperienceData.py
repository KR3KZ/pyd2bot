from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.context.fight.FightResultAdditionalData import FightResultAdditionalData


@dataclass
class FightResultExperienceData(FightResultAdditionalData):
    experience:int
    experienceLevelFloor:int
    experienceNextLevelFloor:int
    experienceFightDelta:int
    experienceForGuild:int
    experienceForMount:int
    rerollExperienceMul:int
    showExperience:bool
    showExperienceLevelFloor:bool
    showExperienceNextLevelFloor:bool
    showExperienceFightDelta:bool
    showExperienceForGuild:bool
    showExperienceForMount:bool
    isIncarnationExperience:bool
    
    
    def __post_init__(self):
        super().__init__()
    