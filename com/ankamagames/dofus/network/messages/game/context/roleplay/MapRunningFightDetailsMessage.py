from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.fight.GameFightFighterLightInformations import GameFightFighterLightInformations
    from com.ankamagames.dofus.network.types.game.context.fight.GameFightFighterLightInformations import GameFightFighterLightInformations
    


class MapRunningFightDetailsMessage(NetworkMessage):
    fightId:int
    attackers:list['GameFightFighterLightInformations']
    defenders:list['GameFightFighterLightInformations']
    

    def init(self, fightId:int, attackers:list['GameFightFighterLightInformations'], defenders:list['GameFightFighterLightInformations']):
        self.fightId = fightId
        self.attackers = attackers
        self.defenders = defenders
        
        super().__init__()
    
    