from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GuildKickRequestMessage(NetworkMessage):
    kickedId:int
    

    def init(self, kickedId:int):
        self.kickedId = kickedId
        
        super().__init__()
    
    