from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.character.alignment.ActorAlignmentInformations import ActorAlignmentInformations


@dataclass
class ActorExtendedAlignmentInformations(ActorAlignmentInformations):
    honor:int
    honorGradeFloor:int
    honorNextGradeFloor:int
    aggressable:int
    
    
    def __post_init__(self):
        super().__init__()
    