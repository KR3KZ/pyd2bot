from com.ankamagames.dofus.network.messages.game.context.fight.GameFightJoinMessage import GameFightJoinMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.party.NamedPartyTeam import NamedPartyTeam


class GameFightSpectatorJoinMessage(GameFightJoinMessage):
    protocolId = 6927
    namedPartyTeams:NamedPartyTeam
    
