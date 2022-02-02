from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.chat.ChatClientPrivateMessage import ChatClientPrivateMessage
from com.ankamagames.dofus.network.types.game.data.items.ObjectItem import ObjectItem


@dataclass
class ChatClientPrivateWithObjectMessage(ChatClientPrivateMessage):
    objects:list[ObjectItem]
    
    
    def __post_init__(self):
        super().__init__()
    