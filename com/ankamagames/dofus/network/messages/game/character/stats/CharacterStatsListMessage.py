from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.character.characteristic.CharacterCharacteristicsInformations import CharacterCharacteristicsInformations


class CharacterStatsListMessage(INetworkMessage):
    protocolId = 2227
    stats:CharacterCharacteristicsInformations
    
    
