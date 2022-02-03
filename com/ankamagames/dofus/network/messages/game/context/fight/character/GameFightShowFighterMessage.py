from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.fight.GameFightFighterInformations import GameFightFighterInformations
    


class GameFightShowFighterMessage(NetworkMessage):
    informations:'GameFightFighterInformations'
    

    def init(self, informations:'GameFightFighterInformations'):
        self.informations = informations
        
        super().__init__()
    
    