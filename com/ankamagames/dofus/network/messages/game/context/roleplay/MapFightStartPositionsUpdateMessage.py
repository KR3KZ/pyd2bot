from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.fight.FightStartingPositions import FightStartingPositions


@dataclass
class MapFightStartPositionsUpdateMessage(NetworkMessage):
    mapId:int
    fightStartPositions:FightStartingPositions
    
    
    def __post_init__(self):
        super().__init__()
    