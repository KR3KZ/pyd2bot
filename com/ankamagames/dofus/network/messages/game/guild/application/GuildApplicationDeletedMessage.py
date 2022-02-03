from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GuildApplicationDeletedMessage(NetworkMessage):
    deleted:bool
    

    def init(self, deleted:bool):
        self.deleted = deleted
        
        super().__init__()
    
    