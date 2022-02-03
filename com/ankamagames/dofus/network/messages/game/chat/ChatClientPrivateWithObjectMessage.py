from com.ankamagames.dofus.network.messages.game.chat.ChatClientPrivateMessage import ChatClientPrivateMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.data.items.ObjectItem import ObjectItem
    from com.ankamagames.dofus.network.types.common.AbstractPlayerSearchInformation import AbstractPlayerSearchInformation
    


class ChatClientPrivateWithObjectMessage(ChatClientPrivateMessage):
    objects:list['ObjectItem']
    

    def init(self, objects:list['ObjectItem'], receiver:'AbstractPlayerSearchInformation', content:str):
        self.objects = objects
        
        super().__init__(receiver, content)
    
    