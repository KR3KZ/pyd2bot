from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.character.CharacterMinimalPlusLookInformations import CharacterMinimalPlusLookInformations
from com.ankamagames.dofus.network.types.game.context.roleplay.BasicGuildInformations import BasicGuildInformations


@dataclass
class CharacterMinimalGuildInformations(CharacterMinimalPlusLookInformations):
    guild:BasicGuildInformations
    
    
    def __post_init__(self):
        super().__init__()
    