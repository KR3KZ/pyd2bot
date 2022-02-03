from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.character.status.PlayerStatus import PlayerStatus
    


class PlayerStatusUpdateMessage(NetworkMessage):
    accountId:int
    playerId:int
    status:'PlayerStatus'
    

    def init(self, accountId:int, playerId:int, status:'PlayerStatus'):
        self.accountId = accountId
        self.playerId = playerId
        self.status = status
        
        super().__init__()
    
    