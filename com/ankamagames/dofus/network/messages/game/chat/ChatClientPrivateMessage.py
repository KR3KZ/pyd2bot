from com.ankamagames.dofus.network.messages.game.chat.ChatAbstractClientMessage import ChatAbstractClientMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.common.AbstractPlayerSearchInformation import AbstractPlayerSearchInformation
    


class ChatClientPrivateMessage(ChatAbstractClientMessage):
    receiver:'AbstractPlayerSearchInformation'
    

    def init(self, receiver:'AbstractPlayerSearchInformation', content:str):
        self.receiver = receiver
        
        super().__init__(content)
    
    