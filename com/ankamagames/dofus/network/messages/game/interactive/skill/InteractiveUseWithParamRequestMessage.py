from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.interactive.InteractiveUseRequestMessage import InteractiveUseRequestMessage


@dataclass
class InteractiveUseWithParamRequestMessage(InteractiveUseRequestMessage):
    id:int
    
    
    def __post_init__(self):
        super().__init__()
    