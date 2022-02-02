from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.approach.ServerSessionConstant import ServerSessionConstant


@dataclass
class ServerSessionConstantsMessage(NetworkMessage):
    variables:list[ServerSessionConstant]
    
    
    def __post_init__(self):
        super().__init__()
    