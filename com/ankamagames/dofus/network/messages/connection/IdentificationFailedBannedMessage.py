from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.connection.IdentificationFailedMessage import IdentificationFailedMessage


@dataclass
class IdentificationFailedBannedMessage(IdentificationFailedMessage):
    banEndDate:int
    
    
    def __post_init__(self):
        super().__init__()
    