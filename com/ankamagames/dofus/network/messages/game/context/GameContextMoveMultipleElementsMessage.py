from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.EntityMovementInformations import EntityMovementInformations


@dataclass
class GameContextMoveMultipleElementsMessage(NetworkMessage):
    movements:list[EntityMovementInformations]
    
    
    def __post_init__(self):
        super().__init__()
    