from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.character.AbstractCharacterInformation import AbstractCharacterInformation


@dataclass
class CharacterRemodelingInformation(AbstractCharacterInformation):
    name:str
    breed:int
    sex:bool
    cosmeticId:int
    colors:list[int]
    
    
    def __post_init__(self):
        super().__init__()
    