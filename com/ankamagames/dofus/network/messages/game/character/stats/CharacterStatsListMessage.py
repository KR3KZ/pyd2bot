from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.character.characteristic.CharacterCharacteristicsInformations import CharacterCharacteristicsInformations


@dataclass
class CharacterStatsListMessage(NetworkMessage):
    stats:CharacterCharacteristicsInformations
    
    
    def __post_init__(self):
        super().__init__()
    