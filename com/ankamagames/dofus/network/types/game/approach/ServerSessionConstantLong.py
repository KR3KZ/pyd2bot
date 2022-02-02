from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.approach.ServerSessionConstant import ServerSessionConstant


@dataclass
class ServerSessionConstantLong(ServerSessionConstant):
    value:int
    
    
    def __post_init__(self):
        super().__init__()
    