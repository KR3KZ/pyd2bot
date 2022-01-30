from com.ankamagames.dofus.network.messages.game.context.roleplay.fight.arena.GameRolePlayArenaUpdatePlayerInfosMessage import GameRolePlayArenaUpdatePlayerInfosMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.fight.arena.ArenaRankInfos import ArenaRankInfos
from com.ankamagames.dofus.network.types.game.context.roleplay.fight.arena.ArenaRankInfos import ArenaRankInfos


class GameRolePlayArenaUpdatePlayerInfosAllQueuesMessage(GameRolePlayArenaUpdatePlayerInfosMessage):
    protocolId = 6540
    team:ArenaRankInfos
    duel:ArenaRankInfos
    
