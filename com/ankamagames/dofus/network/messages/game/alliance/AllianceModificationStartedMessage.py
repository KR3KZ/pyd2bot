from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class AllianceModificationStartedMessage(NetworkMessage):
    canChangeName:bool
    canChangeTag:bool
    canChangeEmblem:bool
    

    def init(self):
        
        super().__init__()
    
    