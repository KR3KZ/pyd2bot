from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.connection.IdentificationMessage import IdentificationMessage


@dataclass
class IdentificationAccountForceMessage(IdentificationMessage):
    forcedAccountLogin:str
    
    
    def __post_init__(self):
        super().__init__()
    