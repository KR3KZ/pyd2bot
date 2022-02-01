from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.fight.arena.ArenaRanking import ArenaRanking
from com.ankamagames.dofus.network.types.game.context.roleplay.fight.arena.ArenaLeagueRanking import ArenaLeagueRanking


class ArenaRankInfos(INetworkMessage):
    protocolId = 750
    ranking:ArenaRanking
    leagueRanking:ArenaLeagueRanking
    victoryCount:int
    fightcount:int
    numFightNeededForLadder:int
    
    
