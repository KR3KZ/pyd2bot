from com.ankamagames.dofus.network.messages.game.context.fight.GameFightJoinMessage import GameFightJoinMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.party.NamedPartyTeam import NamedPartyTeam
    


class GameFightSpectatorJoinMessage(GameFightJoinMessage):
    namedPartyTeams:list['NamedPartyTeam']
    

    def init(self, namedPartyTeams:list['NamedPartyTeam'], timeMaxBeforeFightStart:int, fightType:int):
        self.namedPartyTeams = namedPartyTeams
        
        super().__init__(timeMaxBeforeFightStart, fightType)
    
    