from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ChatSmileyMessage(NetworkMessage):
    entityId:int
    smileyId:int
    accountId:int
    

    def init(self, entityId:int, smileyId:int, accountId:int):
        self.entityId = entityId
        self.smileyId = smileyId
        self.accountId = accountId
        
        super().__init__()
    
    