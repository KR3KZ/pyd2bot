from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameActionFightCastRequestMessage(NetworkMessage):
    spellId:int
    cellId:int
    

    def init(self, spellId:int, cellId:int):
        self.spellId = spellId
        self.cellId = cellId
        
        super().__init__()
    
    