from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.fight.FightResultListEntry import FightResultListEntry
    from com.ankamagames.dofus.network.types.game.context.roleplay.party.NamedPartyTeamWithOutcome import NamedPartyTeamWithOutcome
    


class GameFightEndMessage(NetworkMessage):
    duration:int
    rewardRate:int
    lootShareLimitMalus:int
    results:list['FightResultListEntry']
    namedPartyTeamsOutcomes:list['NamedPartyTeamWithOutcome']
    

    def init(self, duration:int, rewardRate:int, lootShareLimitMalus:int, results:list['FightResultListEntry'], namedPartyTeamsOutcomes:list['NamedPartyTeamWithOutcome']):
        self.duration = duration
        self.rewardRate = rewardRate
        self.lootShareLimitMalus = lootShareLimitMalus
        self.results = results
        self.namedPartyTeamsOutcomes = namedPartyTeamsOutcomes
        
        super().__init__()
    
    