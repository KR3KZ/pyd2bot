from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class GameServerInformations(NetworkMessage):
    id:int
    type:int
    status:int
    completion:int
    charactersCount:int
    charactersSlots:int
    date:int
    isMonoAccount:bool
    isSelectable:bool
    
    
    def __post_init__(self):
        super().__init__()
    