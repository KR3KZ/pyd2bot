from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class NamedPartyTeam(NetworkMessage):
    teamId:int
    partyName:str
    
    
    def __post_init__(self):
        super().__init__()
    