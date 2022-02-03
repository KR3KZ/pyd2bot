from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.fight.FightTeamLightInformations import FightTeamLightInformations
    from com.ankamagames.dofus.network.types.game.context.fight.FightOptionsInformations import FightOptionsInformations
    


class FightExternalInformations(NetworkMessage):
    fightId:int
    fightType:int
    fightStart:int
    fightSpectatorLocked:bool
    fightTeams:list['FightTeamLightInformations']
    fightTeamsOptions:list['FightOptionsInformations']
    

    def init(self, fightId:int, fightType:int, fightStart:int, fightSpectatorLocked:bool, fightTeams:list['FightTeamLightInformations'], fightTeamsOptions:list['FightOptionsInformations']):
        self.fightId = fightId
        self.fightType = fightType
        self.fightStart = fightStart
        self.fightSpectatorLocked = fightSpectatorLocked
        self.fightTeams = fightTeams
        self.fightTeamsOptions = fightTeamsOptions
        
        super().__init__()
    
    