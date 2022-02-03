from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.prism.PrismSubareaEmptyInfo import PrismSubareaEmptyInfo
    


class PrismsListMessage(NetworkMessage):
    prisms:list['PrismSubareaEmptyInfo']
    

    def init(self, prisms:list['PrismSubareaEmptyInfo']):
        self.prisms = prisms
        
        super().__init__()
    
    