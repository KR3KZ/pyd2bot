from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class MapFightCountMessage(NetworkMessage):
    fightCount:int
    

    def init(self, fightCount:int):
        self.fightCount = fightCount
        
        super().__init__()
    
    