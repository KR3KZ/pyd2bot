from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GuildMemberSetWarnOnConnectionMessage(NetworkMessage):
    enable:bool
    

    def init(self, enable:bool):
        self.enable = enable
        
        super().__init__()
    
    