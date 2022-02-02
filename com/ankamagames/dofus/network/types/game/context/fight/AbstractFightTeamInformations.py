from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class AbstractFightTeamInformations(NetworkMessage):
    teamId:int
    leaderId:int
    teamSide:int
    teamTypeId:int
    nbWaves:int
    
    
    def __post_init__(self):
        super().__init__()
    