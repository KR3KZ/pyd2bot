from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.party.NamedPartyTeam import NamedPartyTeam


class NamedPartyTeamWithOutcome(INetworkMessage):
    protocolId = 5095
    team:NamedPartyTeam
    outcome:int
    
    
