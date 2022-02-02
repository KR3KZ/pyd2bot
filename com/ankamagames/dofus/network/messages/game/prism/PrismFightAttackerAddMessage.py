from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.character.CharacterMinimalPlusLookInformations import CharacterMinimalPlusLookInformations


@dataclass
class PrismFightAttackerAddMessage(NetworkMessage):
    subAreaId:int
    fightId:int
    attacker:CharacterMinimalPlusLookInformations
    
    
    def __post_init__(self):
        super().__init__()
    