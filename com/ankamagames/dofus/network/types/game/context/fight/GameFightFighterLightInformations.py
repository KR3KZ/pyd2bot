from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class GameFightFighterLightInformations(NetworkMessage):
    id:int
    wave:int
    level:int
    breed:int
    sex:bool
    alive:bool
    
    
    def __post_init__(self):
        super().__init__()
    