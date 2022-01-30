from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.character.characteristic.CharacterCharacteristicsInformations import CharacterCharacteristicsInformations


class FighterStatsListMessage(NetworkMessage):
    protocolId = 534
    stats:CharacterCharacteristicsInformations
    
    
