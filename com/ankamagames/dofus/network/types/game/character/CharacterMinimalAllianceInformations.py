from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.character.CharacterMinimalGuildInformations import CharacterMinimalGuildInformations
from com.ankamagames.dofus.network.types.game.context.roleplay.BasicAllianceInformations import BasicAllianceInformations


@dataclass
class CharacterMinimalAllianceInformations(CharacterMinimalGuildInformations):
    alliance:BasicAllianceInformations
    
    
    def __post_init__(self):
        super().__init__()
    