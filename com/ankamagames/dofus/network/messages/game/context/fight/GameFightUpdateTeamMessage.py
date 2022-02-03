from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.fight.FightTeamInformations import FightTeamInformations
    


class GameFightUpdateTeamMessage(NetworkMessage):
    fightId:int
    team:'FightTeamInformations'
    

    def init(self, fightId:int, team:'FightTeamInformations'):
        self.fightId = fightId
        self.team = team
        
        super().__init__()
    
    