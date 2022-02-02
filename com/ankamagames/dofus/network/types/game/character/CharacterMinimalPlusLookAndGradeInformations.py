from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.character.CharacterMinimalPlusLookInformations import CharacterMinimalPlusLookInformations


@dataclass
class CharacterMinimalPlusLookAndGradeInformations(CharacterMinimalPlusLookInformations):
    grade:int
    
    
    def __post_init__(self):
        super().__init__()
    