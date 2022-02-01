from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.fight.arena.ArenaRankInfos import ArenaRankInfos


class GameRolePlayArenaUpdatePlayerInfosMessage(NetworkMessage):
    solo:ArenaRankInfos
    
    
