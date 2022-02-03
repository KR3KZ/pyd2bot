from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameMapMovementRequestMessage(NetworkMessage):
    keyMovements:list[int]
    mapId:int
    

    def init(self, keyMovements:list[int], mapId:int):
        self.keyMovements = keyMovements
        self.mapId = mapId
        
        super().__init__()
    
    