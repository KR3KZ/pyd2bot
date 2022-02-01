from com.ankamagames.dofus.network.messages.game.chat.ChatClientMultiMessage import ChatClientMultiMessage
from com.ankamagames.dofus.network.types.game.data.items.ObjectItem import ObjectItem


class ChatClientMultiWithObjectMessage(ChatClientMultiMessage):
    objects:list[ObjectItem]
    
    
