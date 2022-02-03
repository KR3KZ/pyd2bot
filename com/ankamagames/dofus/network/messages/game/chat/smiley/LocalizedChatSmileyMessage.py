from com.ankamagames.dofus.network.messages.game.chat.smiley.ChatSmileyMessage import ChatSmileyMessage


class LocalizedChatSmileyMessage(ChatSmileyMessage):
    cellId:int
    

    def init(self, cellId:int, entityId:int, smileyId:int, accountId:int):
        self.cellId = cellId
        
        super().__init__(entityId, smileyId, accountId)
    
    