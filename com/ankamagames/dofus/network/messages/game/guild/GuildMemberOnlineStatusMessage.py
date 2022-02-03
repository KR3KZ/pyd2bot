from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GuildMemberOnlineStatusMessage(NetworkMessage):
    memberId:int
    online:bool
    

    def init(self, memberId:int, online:bool):
        self.memberId = memberId
        self.online = online
        
        super().__init__()
    
    