from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.character.choice.CharacterBaseInformations import CharacterBaseInformations


class BasicCharactersListMessage(INetworkMessage):
    protocolId = 8228
    characters:CharacterBaseInformations
    
    
