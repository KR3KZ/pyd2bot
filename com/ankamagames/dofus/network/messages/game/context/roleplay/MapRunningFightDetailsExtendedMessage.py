from com.ankamagames.dofus.network.messages.game.context.roleplay.MapRunningFightDetailsMessage import MapRunningFightDetailsMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.party.NamedPartyTeam import NamedPartyTeam


class MapRunningFightDetailsExtendedMessage(MapRunningFightDetailsMessage):
    protocolId = 9456
    namedPartyTeams:NamedPartyTeam
    
