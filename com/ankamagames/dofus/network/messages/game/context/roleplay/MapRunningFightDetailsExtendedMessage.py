from com.ankamagames.dofus.network.messages.game.context.roleplay.MapRunningFightDetailsMessage import MapRunningFightDetailsMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.party.NamedPartyTeam import NamedPartyTeam
    from com.ankamagames.dofus.network.types.game.context.fight.GameFightFighterLightInformations import GameFightFighterLightInformations
    from com.ankamagames.dofus.network.types.game.context.fight.GameFightFighterLightInformations import GameFightFighterLightInformations
    


class MapRunningFightDetailsExtendedMessage(MapRunningFightDetailsMessage):
    namedPartyTeams:list['NamedPartyTeam']
    

    def init(self, namedPartyTeams:list['NamedPartyTeam'], fightId:int, attackers:list['GameFightFighterLightInformations'], defenders:list['GameFightFighterLightInformations']):
        self.namedPartyTeams = namedPartyTeams
        
        super().__init__(fightId, attackers, defenders)
    
    