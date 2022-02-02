from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.chat.ChatServerMessage import ChatServerMessage
from com.ankamagames.dofus.network.types.game.data.items.ObjectItem import ObjectItem


@dataclass
class ChatServerWithObjectMessage(ChatServerMessage):
    objects:list[ObjectItem]
    
    
    def __post_init__(self):
        super().__init__()
    