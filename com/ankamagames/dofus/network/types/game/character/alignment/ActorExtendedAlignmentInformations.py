from com.ankamagames.dofus.network.types.game.character.alignment.ActorAlignmentInformations import ActorAlignmentInformations


class ActorExtendedAlignmentInformations(ActorAlignmentInformations):
    protocolId = 4302
    honor:int
    honorGradeFloor:int
    honorNextGradeFloor:int
    aggressable:int
    
