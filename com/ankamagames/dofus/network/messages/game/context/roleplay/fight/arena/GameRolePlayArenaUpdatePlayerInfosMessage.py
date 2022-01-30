from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.fight.arena.ArenaRankInfos import ArenaRankInfos


class GameRolePlayArenaUpdatePlayerInfosMessage(NetworkMessage):
    protocolId = 8202
    solo:ArenaRankInfos
    
