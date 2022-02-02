from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.character.choice.CharacterBaseInformations import CharacterBaseInformations


@dataclass
class CharacterHardcoreOrEpicInformations(CharacterBaseInformations):
    deathState:int
    deathCount:int
    deathMaxLevel:int
    
    
    def __post_init__(self):
        super().__init__()
    