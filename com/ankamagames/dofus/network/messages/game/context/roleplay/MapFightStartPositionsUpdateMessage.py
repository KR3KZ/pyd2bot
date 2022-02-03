from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.fight.FightStartingPositions import FightStartingPositions
    


class MapFightStartPositionsUpdateMessage(NetworkMessage):
    mapId:int
    fightStartPositions:'FightStartingPositions'
    

    def init(self, mapId:int, fightStartPositions:'FightStartingPositions'):
        self.mapId = mapId
        self.fightStartPositions = fightStartPositions
        
        super().__init__()
    
    