from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.authorized.AdminCommandMessage import AdminCommandMessage


@dataclass
class AdminQuietCommandMessage(AdminCommandMessage):
    
    
    def __post_init__(self):
        super().__init__()
    