from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.character.choice.CharacterRemodelingInformation import CharacterRemodelingInformation


@dataclass
class CharacterToRemodelInformations(CharacterRemodelingInformation):
    possibleChangeMask:int
    mandatoryChangeMask:int
    
    
    def __post_init__(self):
        super().__init__()
    