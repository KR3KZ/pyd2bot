from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.fight.FightTeamInformations import FightTeamInformations
    from com.ankamagames.dofus.network.types.game.context.fight.FightOptionsInformations import FightOptionsInformations
    


class FightCommonInformations(NetworkMessage):
    fightId:int
    fightType:int
    fightTeams:list['FightTeamInformations']
    fightTeamsPositions:list[int]
    fightTeamsOptions:list['FightOptionsInformations']
    

    def init(self, fightId:int, fightType:int, fightTeams:list['FightTeamInformations'], fightTeamsPositions:list[int], fightTeamsOptions:list['FightOptionsInformations']):
        self.fightId = fightId
        self.fightType = fightType
        self.fightTeams = fightTeams
        self.fightTeamsPositions = fightTeamsPositions
        self.fightTeamsOptions = fightTeamsOptions
        
        super().__init__()
    
    