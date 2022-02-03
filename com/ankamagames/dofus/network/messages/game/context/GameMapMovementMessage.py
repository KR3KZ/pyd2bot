from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameMapMovementMessage(NetworkMessage):
    keyMovements:list[int]
    forcedDirection:int
    actorId:int
    

    def init(self, keyMovements:list[int], forcedDirection:int, actorId:int):
        self.keyMovements = keyMovements
        self.forcedDirection = forcedDirection
        self.actorId = actorId
        
        super().__init__()
    
    