from com.ankamagames.dofus.network.messages.game.chat.ChatServerMessage import ChatServerMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.data.items.ObjectItem import ObjectItem
    


class ChatServerWithObjectMessage(ChatServerMessage):
    objects:list['ObjectItem']
    

    def init(self, objects:list['ObjectItem'], senderId:int, senderName:str, prefix:str, senderAccountId:int, channel:int, content:str, timestamp:int, fingerprint:str):
        self.objects = objects
        
        super().__init__(senderId, senderName, prefix, senderAccountId, channel, content, timestamp, fingerprint)
    
    