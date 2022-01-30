from com.ankamagames.dofus.network.messages.game.chat.ChatAbstractServerMessage import ChatAbstractServerMessage


class ChatServerCopyMessage(ChatAbstractServerMessage):
    protocolId = 5344
    receiverId:float
    receiverName:str
    
