from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.character.AbstractCharacterInformation import AbstractCharacterInformation


@dataclass
class CharacterBasicMinimalInformations(AbstractCharacterInformation):
    name:str
    
    
    def __post_init__(self):
        super().__init__()
    