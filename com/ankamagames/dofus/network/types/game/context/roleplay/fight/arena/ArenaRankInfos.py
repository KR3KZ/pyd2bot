from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.fight.arena.ArenaRanking import ArenaRanking
from com.ankamagames.dofus.network.types.game.context.roleplay.fight.arena.ArenaLeagueRanking import ArenaLeagueRanking


@dataclass
class ArenaRankInfos(NetworkMessage):
    victoryCount:int
    fightcount:int
    numFightNeededForLadder:int
    ranking:ArenaRanking = None
    leagueRanking:ArenaLeagueRanking = None
    
    
    def __post_init__(self):
        super().__init__()
    