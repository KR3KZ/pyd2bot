from com.ankamagames.dofus.network.messages.game.context.fight.GameFightEndMessage import GameFightEndMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.fight.FightResultListEntry import FightResultListEntry
    from com.ankamagames.dofus.network.types.game.context.roleplay.party.NamedPartyTeamWithOutcome import NamedPartyTeamWithOutcome
    


class BreachGameFightEndMessage(GameFightEndMessage):
    budget:int
    

    def init(self, budget:int, duration:int, rewardRate:int, lootShareLimitMalus:int, results:list['FightResultListEntry'], namedPartyTeamsOutcomes:list['NamedPartyTeamWithOutcome']):
        self.budget = budget
        
        super().__init__(duration, rewardRate, lootShareLimitMalus, results, namedPartyTeamsOutcomes)
    
    