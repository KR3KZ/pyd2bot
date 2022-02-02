from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.character.CharacterMinimalPlusLookInformations import CharacterMinimalPlusLookInformations


@dataclass
class CharacterBaseInformations(CharacterMinimalPlusLookInformations):
    sex:bool
    
    
    def __post_init__(self):
        super().__init__()
    