from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class GameRolePlayArenaLeagueRewardsMessage(NetworkMessage):
    seasonId:int
    leagueId:int
    ladderPosition:int
    endSeasonReward:bool
    
    
    def __post_init__(self):
        super().__init__()
    