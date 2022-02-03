from com.ankamagames.dofus.network.messages.game.context.GameMapMovementMessage import GameMapMovementMessage


class GameCautiousMapMovementMessage(GameMapMovementMessage):
    

    def init(self, keyMovements:list[int], forcedDirection:int, actorId:int):
        
        super().__init__(keyMovements, forcedDirection, actorId)
    
    