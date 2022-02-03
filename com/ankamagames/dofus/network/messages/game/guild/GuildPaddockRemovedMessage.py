from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GuildPaddockRemovedMessage(NetworkMessage):
    paddockId:int
    

    def init(self, paddockId:int):
        self.paddockId = paddockId
        
        super().__init__()
    
    