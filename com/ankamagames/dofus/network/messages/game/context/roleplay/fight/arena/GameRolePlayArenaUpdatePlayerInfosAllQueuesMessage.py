from com.ankamagames.dofus.network.messages.game.context.roleplay.fight.arena.GameRolePlayArenaUpdatePlayerInfosMessage import GameRolePlayArenaUpdatePlayerInfosMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.fight.arena.ArenaRankInfos import ArenaRankInfos
    from com.ankamagames.dofus.network.types.game.context.roleplay.fight.arena.ArenaRankInfos import ArenaRankInfos
    from com.ankamagames.dofus.network.types.game.context.roleplay.fight.arena.ArenaRankInfos import ArenaRankInfos
    


class GameRolePlayArenaUpdatePlayerInfosAllQueuesMessage(GameRolePlayArenaUpdatePlayerInfosMessage):
    team:'ArenaRankInfos'
    duel:'ArenaRankInfos'
    

    def init(self, team:'ArenaRankInfos', duel:'ArenaRankInfos', solo:'ArenaRankInfos'):
        self.team = team
        self.duel = duel
        
        super().__init__(solo)
    
    