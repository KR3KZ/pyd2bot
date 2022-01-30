from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.party.NamedPartyTeam import NamedPartyTeam


class NamedPartyTeamWithOutcome(NetworkMessage):
    protocolId = 5095
    team:NamedPartyTeam
    outcome:int
    
