from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.chat.ChatAbstractClientMessage import ChatAbstractClientMessage


@dataclass
class ChatClientMultiMessage(ChatAbstractClientMessage):
    channel:int
    
    
    def __post_init__(self):
        super().__init__()
    