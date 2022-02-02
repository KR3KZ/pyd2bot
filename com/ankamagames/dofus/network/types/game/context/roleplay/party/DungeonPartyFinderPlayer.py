from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class DungeonPartyFinderPlayer(NetworkMessage):
    playerId:int
    playerName:str
    breed:int
    sex:bool
    level:int
    
    
    def __post_init__(self):
        super().__init__()
    