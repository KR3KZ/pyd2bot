from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.chat.ChatAbstractServerMessage import ChatAbstractServerMessage


@dataclass
class ChatServerCopyMessage(ChatAbstractServerMessage):
    receiverId:int
    receiverName:str
    
    
    def __post_init__(self):
        super().__init__()
    