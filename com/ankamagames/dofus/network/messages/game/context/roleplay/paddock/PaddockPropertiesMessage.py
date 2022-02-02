from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.paddock.PaddockInstancesInformations import PaddockInstancesInformations


@dataclass
class PaddockPropertiesMessage(NetworkMessage):
    properties:PaddockInstancesInformations
    
    
    def __post_init__(self):
        super().__init__()
    