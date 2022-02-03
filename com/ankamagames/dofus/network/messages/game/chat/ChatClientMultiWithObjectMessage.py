from com.ankamagames.dofus.network.messages.game.chat.ChatClientMultiMessage import ChatClientMultiMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.data.items.ObjectItem import ObjectItem
    


class ChatClientMultiWithObjectMessage(ChatClientMultiMessage):
    objects:list['ObjectItem']
    

    def init(self, objects:list['ObjectItem'], channel:int, content:str):
        self.objects = objects
        
        super().__init__(channel, content)
    
    