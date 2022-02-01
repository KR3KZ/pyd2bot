from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.context.fight.FightResultListEntry import FightResultListEntry
from com.ankamagames.dofus.network.types.game.context.roleplay.party.NamedPartyTeamWithOutcome import NamedPartyTeamWithOutcome


class GameFightEndMessage(INetworkMessage):
    protocolId = 5098
    duration:int
    rewardRate:int
    lootShareLimitMalus:int
    results:FightResultListEntry
    namedPartyTeamsOutcomes:NamedPartyTeamWithOutcome
    
    
