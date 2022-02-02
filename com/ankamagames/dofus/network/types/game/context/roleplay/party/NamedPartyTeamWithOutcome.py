from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.party.NamedPartyTeam import NamedPartyTeam


@dataclass
class NamedPartyTeamWithOutcome(NetworkMessage):
    team:NamedPartyTeam
    outcome:int
    
    
    def __post_init__(self):
        super().__init__()
    