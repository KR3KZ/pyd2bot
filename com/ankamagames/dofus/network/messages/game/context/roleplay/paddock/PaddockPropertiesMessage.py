from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.paddock.PaddockInstancesInformations import PaddockInstancesInformations
    


class PaddockPropertiesMessage(NetworkMessage):
    properties:'PaddockInstancesInformations'
    

    def init(self, properties:'PaddockInstancesInformations'):
        self.properties = properties
        
        super().__init__()
    
    