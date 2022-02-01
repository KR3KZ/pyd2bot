from com.ankamagames.dofus.network.messages.game.character.choice.CharactersListMessage import CharactersListMessage
from com.ankamagames.dofus.network.types.game.character.choice.CharacterToRemodelInformations import CharacterToRemodelInformations


class CharactersListWithRemodelingMessage(CharactersListMessage):
    charactersToRemodel:list[CharacterToRemodelInformations]
    
    
