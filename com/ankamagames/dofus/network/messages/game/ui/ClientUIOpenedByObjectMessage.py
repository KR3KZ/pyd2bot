from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.ui.ClientUIOpenedMessage import ClientUIOpenedMessage


@dataclass
class ClientUIOpenedByObjectMessage(ClientUIOpenedMessage):
    uid:int
    
    
    def __post_init__(self):
        super().__init__()
    