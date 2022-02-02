from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.character.choice.CharactersListMessage import CharactersListMessage
from com.ankamagames.dofus.network.types.game.character.choice.CharacterToRemodelInformations import CharacterToRemodelInformations


@dataclass
class CharactersListWithRemodelingMessage(CharactersListMessage):
    charactersToRemodel:list[CharacterToRemodelInformations]
    
    
    def __post_init__(self):
        super().__init__()
    