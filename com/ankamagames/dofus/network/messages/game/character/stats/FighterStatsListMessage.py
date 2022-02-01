from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.character.characteristic.CharacterCharacteristicsInformations import CharacterCharacteristicsInformations


class FighterStatsListMessage(NetworkMessage):
    stats:CharacterCharacteristicsInformations
    
    
