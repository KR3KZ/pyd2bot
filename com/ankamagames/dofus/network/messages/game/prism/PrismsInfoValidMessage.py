from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.prism.PrismFightersInformation import PrismFightersInformation
    


class PrismsInfoValidMessage(NetworkMessage):
    fights:list['PrismFightersInformation']
    

    def init(self, fights:list['PrismFightersInformation']):
        self.fights = fights
        
        super().__init__()
    
    