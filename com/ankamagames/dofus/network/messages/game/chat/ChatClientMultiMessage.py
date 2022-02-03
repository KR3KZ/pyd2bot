from com.ankamagames.dofus.network.messages.game.chat.ChatAbstractClientMessage import ChatAbstractClientMessage


class ChatClientMultiMessage(ChatAbstractClientMessage):
    channel:int
    

    def init(self, channel:int, content:str):
        self.channel = channel
        
        super().__init__(content)
    
    