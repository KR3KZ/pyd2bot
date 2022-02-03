from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GuildModificationStartedMessage(NetworkMessage):
    canChangeName:bool
    canChangeEmblem:bool
    

    def init(self):
        
        super().__init__()
    
    