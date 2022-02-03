from com.ankamagames.dofus.network.messages.game.chat.ChatServerMessage import ChatServerMessage


class ChatAdminServerMessage(ChatServerMessage):
    

    def init(self, senderId:int, senderName:str, prefix:str, senderAccountId:int, channel:int, content:str, timestamp:int, fingerprint:str):
        
        super().__init__(senderId, senderName, prefix, senderAccountId, channel, content, timestamp, fingerprint)
    
    