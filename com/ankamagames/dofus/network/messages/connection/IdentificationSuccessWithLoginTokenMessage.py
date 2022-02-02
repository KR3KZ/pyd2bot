from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.connection.IdentificationSuccessMessage import IdentificationSuccessMessage


@dataclass
class IdentificationSuccessWithLoginTokenMessage(IdentificationSuccessMessage):
    loginToken:str
    
    
    def __post_init__(self):
        super().__init__()
    