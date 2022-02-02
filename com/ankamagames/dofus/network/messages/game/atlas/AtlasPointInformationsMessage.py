from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.AtlasPointsInformations import AtlasPointsInformations


@dataclass
class AtlasPointInformationsMessage(NetworkMessage):
    type:AtlasPointsInformations
    
    
    def __post_init__(self):
        super().__init__()
    