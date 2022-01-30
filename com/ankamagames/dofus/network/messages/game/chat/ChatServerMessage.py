from com.ankamagames.dofus.network.messages.game.chat.ChatAbstractServerMessage import ChatAbstractServerMessage


class ChatServerMessage(ChatAbstractServerMessage):
    protocolId = 8853
    senderId:int
    senderName:str
    prefix:str
    senderAccountId:int
    
