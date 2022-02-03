from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class NpcDialogReplyMessage(NetworkMessage):
    replyId:int
    

    def init(self, replyId:int):
        self.replyId = replyId
        
        super().__init__()
    
    