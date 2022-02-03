from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class CharacterCanBeCreatedResultMessage(NetworkMessage):
    yesYouCan:bool
    

    def init(self, yesYouCan:bool):
        self.yesYouCan = yesYouCan
        
        super().__init__()
    
    