from com.ankamagames.dofus.network.types.game.context.fight.FightResultAdditionalData import FightResultAdditionalData


class FightResultExperienceData(FightResultAdditionalData):
    protocolId = 9530
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
    
    
