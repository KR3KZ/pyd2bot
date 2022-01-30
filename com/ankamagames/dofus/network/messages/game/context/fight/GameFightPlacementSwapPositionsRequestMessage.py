from com.ankamagames.dofus.network.messages.game.context.fight.GameFightPlacementPositionRequestMessage import GameFightPlacementPositionRequestMessage


class GameFightPlacementSwapPositionsRequestMessage(GameFightPlacementPositionRequestMessage):
    protocolId = 7699
    requestedId:int
    
    
