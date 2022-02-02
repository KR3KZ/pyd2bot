from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.ActorOrientation import ActorOrientation


@dataclass
class GameMapChangeOrientationMessage(NetworkMessage):
    orientation:ActorOrientation
    
    
    def __post_init__(self):
        super().__init__()
    