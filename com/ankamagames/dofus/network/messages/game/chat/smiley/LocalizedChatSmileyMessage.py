from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.chat.smiley.ChatSmileyMessage import ChatSmileyMessage


@dataclass
class LocalizedChatSmileyMessage(ChatSmileyMessage):
    cellId:int
    
    
    def __post_init__(self):
        super().__init__()
    