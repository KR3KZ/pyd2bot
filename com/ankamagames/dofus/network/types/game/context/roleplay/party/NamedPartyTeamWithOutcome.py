from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.party.NamedPartyTeam import NamedPartyTeam


class NamedPartyTeamWithOutcome(NetworkMessage):
    team:NamedPartyTeam
    outcome:int
    
    
