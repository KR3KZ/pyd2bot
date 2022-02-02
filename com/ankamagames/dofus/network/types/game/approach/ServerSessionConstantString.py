from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.approach.ServerSessionConstant import ServerSessionConstant


@dataclass
class ServerSessionConstantString(ServerSessionConstant):
    value:str
    
    
    def __post_init__(self):
        super().__init__()
    