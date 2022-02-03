from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class MoodSmileyResultMessage(NetworkMessage):
    resultCode:int
    smileyId:int
    

    def init(self, resultCode:int, smileyId:int):
        self.resultCode = resultCode
        self.smileyId = smileyId
        
        super().__init__()
    
    