from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.context.roleplay.MapRunningFightDetailsMessage import MapRunningFightDetailsMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.party.NamedPartyTeam import NamedPartyTeam


@dataclass
class MapRunningFightDetailsExtendedMessage(MapRunningFightDetailsMessage):
    namedPartyTeams:list[NamedPartyTeam]
    
    
    def __post_init__(self):
        super().__init__()
    