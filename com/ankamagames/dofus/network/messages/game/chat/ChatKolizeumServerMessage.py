from com.ankamagames.dofus.network.messages.game.chat.ChatServerMessage import ChatServerMessage


class ChatKolizeumServerMessage(ChatServerMessage):
    originServerId:int
    

    def init(self, originServerId:int, senderId:int, senderName:str, prefix:str, senderAccountId:int, channel:int, content:str, timestamp:int, fingerprint:str):
        self.originServerId = originServerId
        
        super().__init__(senderId, senderName, prefix, senderAccountId, channel, content, timestamp, fingerprint)
    
    