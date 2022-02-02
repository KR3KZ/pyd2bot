from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.fight.GameFightCharacteristics import GameFightCharacteristics


@dataclass
class RefreshCharacterStatsMessage(NetworkMessage):
    fighterId:int
    stats:GameFightCharacteristics
    
    
    def __post_init__(self):
        super().__init__()
    