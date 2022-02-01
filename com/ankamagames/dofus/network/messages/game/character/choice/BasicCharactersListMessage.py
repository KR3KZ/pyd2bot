from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.character.choice.CharacterBaseInformations import CharacterBaseInformations


class BasicCharactersListMessage(NetworkMessage):
    characters:list[CharacterBaseInformations]
    
    
