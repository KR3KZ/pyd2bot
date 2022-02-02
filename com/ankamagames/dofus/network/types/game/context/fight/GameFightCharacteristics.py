from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.character.characteristic.CharacterCharacteristics import CharacterCharacteristics


@dataclass
class GameFightCharacteristics(NetworkMessage):
    characteristics:CharacterCharacteristics
    summoner:int
    summoned:bool
    invisibilityState:int
    
    
    def __post_init__(self):
        super().__init__()
    