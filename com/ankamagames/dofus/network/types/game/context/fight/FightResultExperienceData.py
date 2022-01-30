from com.ankamagames.dofus.network.types.game.context.fight.FightResultAdditionalData import FightResultAdditionalData


class FightResultExperienceData(FightResultAdditionalData):
    protocolId = 9530
    experience:float
    experienceLevelFloor:float
    experienceNextLevelFloor:float
    experienceFightDelta:float
    experienceForGuild:float
    experienceForMount:float
    rerollExperienceMul:int
    
