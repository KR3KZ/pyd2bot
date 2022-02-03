from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class TitleSelectRequestMessage(NetworkMessage):
    titleId:int
    

    def init(self, titleId:int):
        self.titleId = titleId
        
        super().__init__()
    
    