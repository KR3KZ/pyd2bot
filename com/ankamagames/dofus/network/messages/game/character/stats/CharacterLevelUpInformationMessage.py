from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.character.stats.CharacterLevelUpMessage import CharacterLevelUpMessage


@dataclass
class CharacterLevelUpInformationMessage(CharacterLevelUpMessage):
    name:str
    id:int
    
    
    def __post_init__(self):
        super().__init__()
    