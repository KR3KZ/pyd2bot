from com.ankamagames.dofus.network.messages.game.chat.ChatAbstractClientMessage import ChatAbstractClientMessage


class ChatClientMultiMessage(ChatAbstractClientMessage):
    protocolId = 1382
    channel:int
    
    
