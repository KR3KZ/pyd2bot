from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.chat.ChatAbstractClientMessage import ChatAbstractClientMessage
from com.ankamagames.dofus.network.types.common.AbstractPlayerSearchInformation import AbstractPlayerSearchInformation


@dataclass
class ChatClientPrivateMessage(ChatAbstractClientMessage):
    receiver:AbstractPlayerSearchInformation
    
    
    def __post_init__(self):
        super().__init__()
    