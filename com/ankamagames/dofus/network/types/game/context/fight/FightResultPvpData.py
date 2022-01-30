from com.ankamagames.dofus.network.types.game.context.fight.FightResultAdditionalData import FightResultAdditionalData


class FightResultPvpData(FightResultAdditionalData):
    protocolId = 9919
    grade:int
    minHonorForGrade:int
    maxHonorForGrade:int
    honor:int
    honorDelta:int
    
