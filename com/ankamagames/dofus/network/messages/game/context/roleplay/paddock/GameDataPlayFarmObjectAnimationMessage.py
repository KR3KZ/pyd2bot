from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameDataPlayFarmObjectAnimationMessage(NetworkMessage):
    cellId:list[int]
    

    def init(self, cellId:list[int]):
        self.cellId = cellId
        
        super().__init__()
    
    