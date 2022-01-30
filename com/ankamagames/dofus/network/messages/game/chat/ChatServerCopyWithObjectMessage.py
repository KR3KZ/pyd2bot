from com.ankamagames.dofus.network.messages.game.chat.ChatServerCopyMessage import ChatServerCopyMessage
from com.ankamagames.dofus.network.types.game.data.items.ObjectItem import ObjectItem


class ChatServerCopyWithObjectMessage(ChatServerCopyMessage):
    protocolId = 9930
    objects:list[ObjectItem]
    
