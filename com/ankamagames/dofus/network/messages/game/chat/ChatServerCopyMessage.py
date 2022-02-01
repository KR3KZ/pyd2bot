from com.ankamagames.dofus.network.messages.game.chat.ChatAbstractServerMessage import ChatAbstractServerMessage


class ChatServerCopyMessage(ChatAbstractServerMessage):
    receiverId:int
    receiverName:str
    
    
