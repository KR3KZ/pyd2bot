from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.EntityMovementInformations import EntityMovementInformations
    


class GameContextMoveElementMessage(NetworkMessage):
    movement:'EntityMovementInformations'
    

    def init(self, movement:'EntityMovementInformations'):
        self.movement = movement
        
        super().__init__()
    
    