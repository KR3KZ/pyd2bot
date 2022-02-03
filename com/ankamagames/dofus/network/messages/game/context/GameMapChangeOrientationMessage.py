from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.ActorOrientation import ActorOrientation
    


class GameMapChangeOrientationMessage(NetworkMessage):
    orientation:'ActorOrientation'
    

    def init(self, orientation:'ActorOrientation'):
        self.orientation = orientation
        
        super().__init__()
    
    