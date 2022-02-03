from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.GameContextActorPositionInformations import GameContextActorPositionInformations
    


class GameContextBasicSpawnInformation(NetworkMessage):
    teamId:int
    alive:bool
    informations:'GameContextActorPositionInformations'
    

    def init(self, teamId:int, alive:bool, informations:'GameContextActorPositionInformations'):
        self.teamId = teamId
        self.alive = alive
        self.informations = informations
        
        super().__init__()
    
    