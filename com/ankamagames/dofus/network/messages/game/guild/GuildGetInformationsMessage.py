from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GuildGetInformationsMessage(NetworkMessage):
    infoType:int
    

    def init(self, infoType:int):
        self.infoType = infoType
        
        super().__init__()
    
    