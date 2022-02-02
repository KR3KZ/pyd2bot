from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.entity.EntityInformation import EntityInformation


@dataclass
class EntitiesInformationMessage(NetworkMessage):
    entities:list[EntityInformation]
    
    
    def __post_init__(self):
        super().__init__()
    