from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.fight.FightResultListEntry import FightResultListEntry
from com.ankamagames.dofus.network.types.game.context.roleplay.party.NamedPartyTeamWithOutcome import NamedPartyTeamWithOutcome


@dataclass
class GameFightEndMessage(NetworkMessage):
    duration:int
    rewardRate:int
    lootShareLimitMalus:int
    results:list[FightResultListEntry]
    namedPartyTeamsOutcomes:list[NamedPartyTeamWithOutcome]
    
    
    def __post_init__(self):
        super().__init__()
    