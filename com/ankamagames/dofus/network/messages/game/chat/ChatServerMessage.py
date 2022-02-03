from com.ankamagames.dofus.network.messages.game.chat.ChatAbstractServerMessage import ChatAbstractServerMessage


class ChatServerMessage(ChatAbstractServerMessage):
    senderId:int
    senderName:str
    prefix:str
    senderAccountId:int
    

    def init(self, senderId:int, senderName:str, prefix:str, senderAccountId:int, channel:int, content:str, timestamp:int, fingerprint:str):
        self.senderId = senderId
        self.senderName = senderName
        self.prefix = prefix
        self.senderAccountId = senderAccountId
        
        super().__init__(channel, content, timestamp, fingerprint)
    
    