from com.ankamagames.dofus.network.messages.game.chat.ChatAbstractServerMessage import ChatAbstractServerMessage


class ChatServerCopyMessage(ChatAbstractServerMessage):
    receiverId:int
    receiverName:str
    

    def init(self, receiverId:int, receiverName:str, channel:int, content:str, timestamp:int, fingerprint:str):
        self.receiverId = receiverId
        self.receiverName = receiverName
        
        super().__init__(channel, content, timestamp, fingerprint)
    
    