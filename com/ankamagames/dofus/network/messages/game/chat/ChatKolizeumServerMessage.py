from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.chat.ChatServerMessage import ChatServerMessage


@dataclass
class ChatKolizeumServerMessage(ChatServerMessage):
    originServerId:int
    
    
    def __post_init__(self):
        super().__init__()
    