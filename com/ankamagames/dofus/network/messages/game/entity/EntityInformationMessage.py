from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.entity.EntityInformation import EntityInformation
    


class EntityInformationMessage(NetworkMessage):
    entity:'EntityInformation'
    

    def init(self, entity:'EntityInformation'):
        self.entity = entity
        
        super().__init__()
    
    