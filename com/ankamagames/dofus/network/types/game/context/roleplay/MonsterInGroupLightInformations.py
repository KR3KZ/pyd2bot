from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class MonsterInGroupLightInformations(NetworkMessage):
    genericId:int
    grade:int
    level:int
    
    
    def __post_init__(self):
        super().__init__()
    