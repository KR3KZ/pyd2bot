from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.web.haapi.HaapiValidationMessage import HaapiValidationMessage


@dataclass
class HaapiBuyValidationMessage(HaapiValidationMessage):
    amount:int
    email:str
    
    
    def __post_init__(self):
        super().__init__()
    