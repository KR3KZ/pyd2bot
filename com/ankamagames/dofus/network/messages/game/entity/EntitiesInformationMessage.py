from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.entity.EntityInformation import EntityInformation
    


class EntitiesInformationMessage(NetworkMessage):
    entities:list['EntityInformation']
    

    def init(self, entities:list['EntityInformation']):
        self.entities = entities
        
        super().__init__()
    
    