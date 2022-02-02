from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.chat.ChatAbstractServerMessage import ChatAbstractServerMessage


@dataclass
class ChatServerMessage(ChatAbstractServerMessage):
    senderId:int
    senderName:str
    prefix:str
    senderAccountId:int
    
    
    def __post_init__(self):
        super().__init__()
    