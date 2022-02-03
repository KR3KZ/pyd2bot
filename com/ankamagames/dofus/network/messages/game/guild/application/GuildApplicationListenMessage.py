from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GuildApplicationListenMessage(NetworkMessage):
    listen:bool
    

    def init(self, listen:bool):
        self.listen = listen
        
        super().__init__()
    
    