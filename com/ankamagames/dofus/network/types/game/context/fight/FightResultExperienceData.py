from com.ankamagames.dofus.network.types.game.context.fight.FightResultAdditionalData import FightResultAdditionalData


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
    

    def init(self, experience:int, experienceLevelFloor:int, experienceNextLevelFloor:int, experienceFightDelta:int, experienceForGuild:int, experienceForMount:int, rerollExperienceMul:int):
        self.experience = experience
        self.experienceLevelFloor = experienceLevelFloor
        self.experienceNextLevelFloor = experienceNextLevelFloor
        self.experienceFightDelta = experienceFightDelta
        self.experienceForGuild = experienceForGuild
        self.experienceForMount = experienceForMount
        self.rerollExperienceMul = rerollExperienceMul
        
        super().__init__()
    
    