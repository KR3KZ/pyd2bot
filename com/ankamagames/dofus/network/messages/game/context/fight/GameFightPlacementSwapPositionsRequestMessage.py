from com.ankamagames.dofus.network.messages.game.context.fight.GameFightPlacementPositionRequestMessage import GameFightPlacementPositionRequestMessage


class GameFightPlacementSwapPositionsRequestMessage(GameFightPlacementPositionRequestMessage):
    requestedId:int
    

    def init(self, requestedId:int, cellId:int):
        self.requestedId = requestedId
        
        super().__init__(cellId)
    
    