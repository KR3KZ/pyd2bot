from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.character.characteristic.CharacterCharacteristicsInformations import CharacterCharacteristicsInformations


class CharacterStatsListMessage(NetworkMessage):
    protocolId = 2227
    stats:CharacterCharacteristicsInformations
    
    
