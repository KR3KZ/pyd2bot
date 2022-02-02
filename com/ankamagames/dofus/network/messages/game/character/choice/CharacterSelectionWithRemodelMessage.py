from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.character.choice.CharacterSelectionMessage import CharacterSelectionMessage
from com.ankamagames.dofus.network.types.game.character.choice.RemodelingInformation import RemodelingInformation


@dataclass
class CharacterSelectionWithRemodelMessage(CharacterSelectionMessage):
    remodel:RemodelingInformation
    
    
    def __post_init__(self):
        super().__init__()
    