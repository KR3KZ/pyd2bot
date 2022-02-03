from com.ankamagames.dofus.network.messages.game.chat.ChatServerCopyMessage import ChatServerCopyMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.data.items.ObjectItem import ObjectItem
    


class ChatServerCopyWithObjectMessage(ChatServerCopyMessage):
    objects:list['ObjectItem']
    

    def init(self, objects:list['ObjectItem'], receiverId:int, receiverName:str, channel:int, content:str, timestamp:int, fingerprint:str):
        self.objects = objects
        
        super().__init__(receiverId, receiverName, channel, content, timestamp, fingerprint)
    
    