from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class NicknameChoiceRequestMessage(NetworkMessage):
    nickname:str
    

    def init(self, nickname:str):
        self.nickname = nickname
        
        super().__init__()
    
    