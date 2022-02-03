from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.fight.arena.ArenaRankInfos import ArenaRankInfos
    


class GameRolePlayArenaUpdatePlayerInfosMessage(NetworkMessage):
    solo:'ArenaRankInfos'
    

    def init(self, solo:'ArenaRankInfos'):
        self.solo = solo
        
        super().__init__()
    
    