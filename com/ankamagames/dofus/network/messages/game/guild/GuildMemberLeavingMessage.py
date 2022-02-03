from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GuildMemberLeavingMessage(NetworkMessage):
    kicked:bool
    memberId:int
    

    def init(self, kicked:bool, memberId:int):
        self.kicked = kicked
        self.memberId = memberId
        
        super().__init__()
    
    