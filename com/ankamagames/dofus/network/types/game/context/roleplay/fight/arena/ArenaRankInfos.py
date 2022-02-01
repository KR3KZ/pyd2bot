from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.fight.arena.ArenaRanking import ArenaRanking
from com.ankamagames.dofus.network.types.game.context.roleplay.fight.arena.ArenaLeagueRanking import ArenaLeagueRanking


class ArenaRankInfos(NetworkMessage):
    ranking:ArenaRanking = None
    leagueRanking:ArenaLeagueRanking = None
    victoryCount:int
    fightcount:int
    numFightNeededForLadder:int
    
    
