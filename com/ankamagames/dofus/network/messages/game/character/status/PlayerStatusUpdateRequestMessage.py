from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.character.status.PlayerStatus import PlayerStatus
    


class PlayerStatusUpdateRequestMessage(NetworkMessage):
    status:'PlayerStatus'
    

    def init(self, status:'PlayerStatus'):
        self.status = status
        
        super().__init__()
    
    