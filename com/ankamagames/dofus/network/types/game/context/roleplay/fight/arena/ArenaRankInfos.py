from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.fight.arena.ArenaRanking import ArenaRanking
    from com.ankamagames.dofus.network.types.game.context.roleplay.fight.arena.ArenaLeagueRanking import ArenaLeagueRanking
    


class ArenaRankInfos(NetworkMessage):
    ranking:'ArenaRanking'
    leagueRanking:'ArenaLeagueRanking'
    victoryCount:int
    fightcount:int
    numFightNeededForLadder:int
    

    def init(self, ranking:'ArenaRanking', leagueRanking:'ArenaLeagueRanking', victoryCount:int, fightcount:int, numFightNeededForLadder:int):
        self.ranking = ranking
        self.leagueRanking = leagueRanking
        self.victoryCount = victoryCount
        self.fightcount = fightcount
        self.numFightNeededForLadder = numFightNeededForLadder
        
        super().__init__()
    
    