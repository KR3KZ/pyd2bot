from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.character.CharacterMinimalPlusLookInformations import CharacterMinimalPlusLookInformations


@dataclass
class PrismFightDefenderAddMessage(NetworkMessage):
    subAreaId:int
    fightId:int
    defender:CharacterMinimalPlusLookInformations
    
    
    def __post_init__(self):
        super().__init__()
    