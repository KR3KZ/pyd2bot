from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.character.choice.CharacterBaseInformations import CharacterBaseInformations


class BasicCharactersListMessage(NetworkMessage):
    protocolId = 8228
    characters:CharacterBaseInformations
    
