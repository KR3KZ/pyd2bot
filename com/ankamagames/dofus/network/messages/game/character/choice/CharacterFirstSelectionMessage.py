from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.character.choice.CharacterSelectionMessage import CharacterSelectionMessage


@dataclass
class CharacterFirstSelectionMessage(CharacterSelectionMessage):
    doTutorial:bool
    
    
    def __post_init__(self):
        super().__init__()
    