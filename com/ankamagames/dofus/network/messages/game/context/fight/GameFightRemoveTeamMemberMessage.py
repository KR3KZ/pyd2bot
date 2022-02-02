from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class GameFightRemoveTeamMemberMessage(NetworkMessage):
    fightId:int
    teamId:int
    charId:int
    
    
    def __post_init__(self):
        super().__init__()
    