from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GameRolePlayArenaLeagueRewardsMessage(NetworkMessage):
    protocolId = 2090
    seasonId:int
    leagueId:int
    ladderPosition:int
    endSeasonReward:bool
    
    
