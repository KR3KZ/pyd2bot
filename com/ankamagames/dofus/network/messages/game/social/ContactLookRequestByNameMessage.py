from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.social.ContactLookRequestMessage import ContactLookRequestMessage


@dataclass
class ContactLookRequestByNameMessage(ContactLookRequestMessage):
    playerName:str
    
    
    def __post_init__(self):
        super().__init__()
    