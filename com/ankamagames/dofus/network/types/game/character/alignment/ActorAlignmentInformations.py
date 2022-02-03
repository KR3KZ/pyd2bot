from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ActorAlignmentInformations(NetworkMessage):
    alignmentSide:int
    alignmentValue:int
    alignmentGrade:int
    characterPower:int
    

    def init(self, alignmentSide:int, alignmentValue:int, alignmentGrade:int, characterPower:int):
        self.alignmentSide = alignmentSide
        self.alignmentValue = alignmentValue
        self.alignmentGrade = alignmentGrade
        self.characterPower = characterPower
        
        super().__init__()
    
    