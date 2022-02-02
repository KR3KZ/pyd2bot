from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.character.CharacterBasicMinimalInformations import CharacterBasicMinimalInformations


@dataclass
class CharacterMinimalInformations(CharacterBasicMinimalInformations):
    level:int
    
    
    def __post_init__(self):
        super().__init__()
    