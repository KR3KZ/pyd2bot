from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GuildMemberWarnOnConnectionStateMessage(NetworkMessage):
    enable:bool
    

    def init(self, enable:bool):
        self.enable = enable
        
        super().__init__()
    
    