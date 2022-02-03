from com.ankamagames.dofus.network.types.game.character.alignment.ActorAlignmentInformations import ActorAlignmentInformations


class ActorExtendedAlignmentInformations(ActorAlignmentInformations):
    honor:int
    honorGradeFloor:int
    honorNextGradeFloor:int
    aggressable:int
    

    def init(self, honor:int, honorGradeFloor:int, honorNextGradeFloor:int, aggressable:int, alignmentSide:int, alignmentValue:int, alignmentGrade:int, characterPower:int):
        self.honor = honor
        self.honorGradeFloor = honorGradeFloor
        self.honorNextGradeFloor = honorNextGradeFloor
        self.aggressable = aggressable
        
        super().__init__(alignmentSide, alignmentValue, alignmentGrade, characterPower)
    
    