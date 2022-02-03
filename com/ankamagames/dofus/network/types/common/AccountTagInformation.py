from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class AccountTagInformation(NetworkMessage):
    nickname:str
    tagNumber:str
    

    def init(self, nickname:str, tagNumber:str):
        self.nickname = nickname
        self.tagNumber = tagNumber
        
        super().__init__()
    
    