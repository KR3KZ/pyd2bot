from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.IdentifiedEntityDispositionInformations import IdentifiedEntityDispositionInformations
    


class GameEntityDispositionMessage(NetworkMessage):
    disposition:'IdentifiedEntityDispositionInformations'
    

    def init(self, disposition:'IdentifiedEntityDispositionInformations'):
        self.disposition = disposition
        
        super().__init__()
    
    