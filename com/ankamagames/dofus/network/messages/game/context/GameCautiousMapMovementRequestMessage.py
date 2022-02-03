from com.ankamagames.dofus.network.messages.game.context.GameMapMovementRequestMessage import GameMapMovementRequestMessage


class GameCautiousMapMovementRequestMessage(GameMapMovementRequestMessage):
    

    def init(self, keyMovements:list[int], mapId:int):
        
        super().__init__(keyMovements, mapId)
    
    