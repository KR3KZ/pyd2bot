from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.idol.Idol import Idol


@dataclass
class GameFightStartMessage(NetworkMessage):
    idols:list[Idol]
    
    
    def __post_init__(self):
        super().__init__()
    