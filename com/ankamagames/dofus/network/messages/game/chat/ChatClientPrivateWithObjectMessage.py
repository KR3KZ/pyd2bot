from com.ankamagames.dofus.network.messages.game.chat.ChatClientPrivateMessage import ChatClientPrivateMessage
from com.ankamagames.dofus.network.types.game.data.items.ObjectItem import ObjectItem


class ChatClientPrivateWithObjectMessage(ChatClientPrivateMessage):
    protocolId = 1043
    objects:ObjectItem
    
    
