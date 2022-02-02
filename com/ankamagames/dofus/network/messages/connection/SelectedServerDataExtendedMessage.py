from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.connection.SelectedServerDataMessage import SelectedServerDataMessage
from com.ankamagames.dofus.network.types.connection.GameServerInformations import GameServerInformations


@dataclass
class SelectedServerDataExtendedMessage(SelectedServerDataMessage):
    servers:list[GameServerInformations]
    
    
    def __post_init__(self):
        super().__init__()
    