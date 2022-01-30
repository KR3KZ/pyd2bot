from com.ankamagames.dofus.network.messages.game.chat.ChatServerMessage import ChatServerMessage


class ChatKolizeumServerMessage(ChatServerMessage):
    protocolId = 4380
    originServerId:int
    
