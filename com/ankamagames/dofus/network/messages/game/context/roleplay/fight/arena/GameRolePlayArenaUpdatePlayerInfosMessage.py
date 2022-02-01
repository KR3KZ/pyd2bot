from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.fight.arena.ArenaRankInfos import ArenaRankInfos


class GameRolePlayArenaUpdatePlayerInfosMessage(INetworkMessage):
    protocolId = 8202
    solo:ArenaRankInfos
    
    
