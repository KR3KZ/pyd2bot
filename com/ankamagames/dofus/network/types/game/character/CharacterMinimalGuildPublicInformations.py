from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.character.CharacterMinimalInformations import CharacterMinimalInformations


@dataclass
class CharacterMinimalGuildPublicInformations(CharacterMinimalInformations):
    rank:int
    
    
    def __post_init__(self):
        super().__init__()
    