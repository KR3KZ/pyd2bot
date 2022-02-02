from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.context.fight.GameFightJoinMessage import GameFightJoinMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.party.NamedPartyTeam import NamedPartyTeam


@dataclass
class GameFightSpectatorJoinMessage(GameFightJoinMessage):
    namedPartyTeams:list[NamedPartyTeam]
    
    
    def __post_init__(self):
        super().__init__()
    