from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.character.characteristic.CharacterCharacteristicsInformations import CharacterCharacteristicsInformations


class CharacterStatsListMessage(NetworkMessage):
    stats:CharacterCharacteristicsInformations
    
    
