from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class UpdateMapPlayersAgressableStatusMessage(NetworkMessage):
    playerIds:list[int]
    enable:list[int]
    
    
    def __post_init__(self):
        super().__init__()
    