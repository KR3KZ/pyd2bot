from com.ankamagames.dofus.network.messages.game.chat.ChatServerMessage import ChatServerMessage
from com.ankamagames.dofus.network.types.game.data.items.ObjectItem import ObjectItem


class ChatServerWithObjectMessage(ChatServerMessage):
    protocolId = 5967
    objects:ObjectItem
    
