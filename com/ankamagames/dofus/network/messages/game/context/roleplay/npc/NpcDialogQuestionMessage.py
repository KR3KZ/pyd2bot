from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class NpcDialogQuestionMessage(NetworkMessage):
    messageId:int
    dialogParams:list[str]
    visibleReplies:list[int]
    

    def init(self, messageId:int, dialogParams:list[str], visibleReplies:list[int]):
        self.messageId = messageId
        self.dialogParams = dialogParams
        self.visibleReplies = visibleReplies
        
        super().__init__()
    
    