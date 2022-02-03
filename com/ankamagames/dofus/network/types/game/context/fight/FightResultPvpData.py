from com.ankamagames.dofus.network.types.game.context.fight.FightResultAdditionalData import FightResultAdditionalData


class FightResultPvpData(FightResultAdditionalData):
    grade:int
    minHonorForGrade:int
    maxHonorForGrade:int
    honor:int
    honorDelta:int
    

    def init(self, grade:int, minHonorForGrade:int, maxHonorForGrade:int, honor:int, honorDelta:int):
        self.grade = grade
        self.minHonorForGrade = minHonorForGrade
        self.maxHonorForGrade = maxHonorForGrade
        self.honor = honor
        self.honorDelta = honorDelta
        
        super().__init__()
    
    