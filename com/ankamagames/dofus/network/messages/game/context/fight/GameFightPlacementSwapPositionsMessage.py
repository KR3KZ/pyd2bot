from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.IdentifiedEntityDispositionInformations import IdentifiedEntityDispositionInformations
    


class GameFightPlacementSwapPositionsMessage(NetworkMessage):
    dispositions:list['IdentifiedEntityDispositionInformations']
    

    def init(self, dispositions:list['IdentifiedEntityDispositionInformations']):
        self.dispositions = dispositions
        
        super().__init__()
    
    