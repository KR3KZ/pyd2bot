from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.finishmoves.FinishMoveInformations import FinishMoveInformations
    


class FinishMoveListMessage(NetworkMessage):
    finishMoves:list['FinishMoveInformations']
    

    def init(self, finishMoves:list['FinishMoveInformations']):
        self.finishMoves = finishMoves
        
        super().__init__()
    
    