from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class GameRolePlayArenaSwitchToFightServerMessage(NetworkMessage):
    address:str
    ports:list[int]
    ticket:list[int]
    
    
    def __post_init__(self):
        super().__init__()
    