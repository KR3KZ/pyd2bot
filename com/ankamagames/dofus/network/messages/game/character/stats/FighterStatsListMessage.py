from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.character.characteristic.CharacterCharacteristicsInformations import CharacterCharacteristicsInformations


class FighterStatsListMessage(INetworkMessage):
    protocolId = 534
    stats:CharacterCharacteristicsInformations
    
    
