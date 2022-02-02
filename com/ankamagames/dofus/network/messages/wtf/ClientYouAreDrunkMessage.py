from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.debug.DebugInClientMessage import DebugInClientMessage


@dataclass
class ClientYouAreDrunkMessage(DebugInClientMessage):
    
    
    def __post_init__(self):
        super().__init__()
    