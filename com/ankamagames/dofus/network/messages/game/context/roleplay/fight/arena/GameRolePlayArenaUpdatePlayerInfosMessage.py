from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.fight.arena.ArenaRankInfos import ArenaRankInfos


@dataclass
class GameRolePlayArenaUpdatePlayerInfosMessage(NetworkMessage):
    solo:ArenaRankInfos
    
    
    def __post_init__(self):
        super().__init__()
    