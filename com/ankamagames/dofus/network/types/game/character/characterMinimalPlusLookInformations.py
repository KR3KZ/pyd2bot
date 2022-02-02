from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.character.CharacterMinimalInformations import CharacterMinimalInformations
from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook


@dataclass
class CharacterMinimalPlusLookInformations(CharacterMinimalInformations):
    entityLook:EntityLook
    breed:int
    
    
    def __post_init__(self):
        super().__init__()
    