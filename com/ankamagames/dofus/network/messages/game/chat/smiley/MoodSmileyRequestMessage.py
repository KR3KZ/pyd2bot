from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class MoodSmileyRequestMessage(NetworkMessage):
    smileyId:int
    

    def init(self, smileyId:int):
        self.smileyId = smileyId
        
        super().__init__()
    
    